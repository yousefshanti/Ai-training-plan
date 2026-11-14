#%%



import os
import numpy as np
import pandas as pd
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
from openai import OpenAI

PDF_PATH = "water_doc.pdf"
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
LLM_MODEL = "openai/gpt-oss-120b"   # llama-3.3-70b-versatile was retired on Groq (404)

# Key lives in .env next to this file (git-ignored), never in this file.
if os.path.exists(".env"):
    for line in open(".env"):
        k, _, v = line.strip().partition("=")
        if k and not k.startswith("#"):
            os.environ.setdefault(k, v)
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

#%%
#  [Task 1] Load PDF content
def load_pdf(path):
    """Return a list of {'page': n, 'text': ...} for every non-empty page."""
    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = " ".join(text.split())          # clean extra spaces/newlines
        if text:
            pages.append({"page": i, "text": text})
    return pages



pages = load_pdf(PDF_PATH)
print(f"Pages with text: {len(pages)}")
print(f"Total words: {sum(len(p['text'].split()) for p in pages)}")
print("\nPreview of page 1:\n", pages[0]["text"][:500])


#%%
# [Task 2] Split text into chunks
def chunk_pages(pages, chunk_size=200, overlap=40):
    """
    Split the whole document into chunks of `chunk_size` words.
    Consecutive chunks share `overlap` words so an idea cut at a boundary
    still appears complete in one of them. Each chunk remembers its page(s).
    """
    words = [(w, p["page"]) for p in pages for w in p["text"].split()]
    step = chunk_size - overlap
    chunks = []
    for start in range(0, len(words), step):
        piece = words[start:start + chunk_size]
        chunks.append({

            "id": len(chunks),
            "text": " ".join(w for w, _ in piece),
            "pages": sorted({pg for _, pg in piece}),
        })
        if start + chunk_size >= len(words):
            break
    return chunks


chunks = chunk_pages(pages, chunk_size=200, overlap=40)
print(f"Number of chunks: {len(chunks)}")
print(f"\nChunk 0 (pages {chunks[0]['pages']}):\n{chunks[0]['text'][:400]}...")


#%%
# [Task 3] Generate embeddings with sentence-transformers
embed_model = SentenceTransformer(EMBED_MODEL_NAME)

chunk_texts = [c["text"] for c in chunks]
embeddings = embed_model.encode(

    chunk_texts,
    normalize_embeddings=True,   # length = 1  ->  dot product == cosine similarity
    show_progress_bar=True,
).astype("float32")

print("Embeddings shape:", embeddings.shape)   # (num_chunks, 384)



#%%
# [Task 4] Store embeddings in a FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatIP(dim)   # IP = inner product (cosine, since vectors are normalized)
index.add(embeddings)

print("Vectors stored in FAISS:", index.ntotal)


# %% [Task 5] Semantic search: retrieve top-k chunks for a query
def search(query, k=3, index=index, chunks=chunks, model=embed_model):
    q_vec = model.encode([query], normalize_embeddings=True).astype("float32")
    scores, ids = index.search(q_vec, k)
    results = []
    for score, idx in zip(scores[0], ids[0]):
        if idx == -1:
            continue
        results.append({**chunks[idx], "score": float(score)})
    return results


test_query = "What is this document about?"
for r in search(test_query, k=3):
    print(f"[chunk {r['id']} | pages {r['pages']} | score {r['score']:.3f}]")
    print(r["text"][:250], "...\n")


#%%
# [Task 6] Integrate retrieved chunks with an LLM (Groq via OpenAI client)
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)  # Groq speaks the OpenAI API; key comes from .env

SYSTEM_PROMPT = (
    "You are an assistant that answers questions about a water-sector document. "
    "Answer ONLY using the provided context. "
    "If the answer is not in the context, reply exactly: "
    "\"I couldn't find this in the document.\" "
    "Be concise and cite the chunk numbers you used, e.g. [chunk 3]."
)


def build_context(retrieved):
    return "\n\n".join(
        f"[chunk {r['id']} | pages {r['pages']}]\n{r['text']}" for r in retrieved
    )


def ask(query, k=3, show_sources=True):
    retrieved = search(query, k=k)
    user_prompt = f"Context:\n{build_context(retrieved)}\n\nQuestion: {query}"

    response = client.chat.completions.create(
        model=LLM_MODEL,
        temperature=0,   # deterministic, less "creative" answers
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )
    answer = response.choices[0].message.content

    print(f"Q: {query}\nA: {answer}")
    if show_sources:
        print("Sources:", [(r["id"], r["pages"], round(r["score"], 3)) for r in retrieved])
    print("-" * 70)
    return answer


ask("What is the main topic of this document?")


#%%
# [Task 7] Test the pipeline with sample questions
# Replace/add questions after reading water_doc.pdf.
sample_questions = [
    "What is the main topic of this document?",
    "What are the main causes of water loss mentioned?",
    "What recommendations does the document give?",
    "What numbers or statistics are mentioned about water consumption?",
    "Who won the 2022 World Cup?",   # out-of-scope -> should say it's not in the document
]

for q in sample_questions:
    ask(q, k=3)


# %%
# [Task 8] Optimize: chunk size, number of retrieved chunks (k), embedding model
# Retrieval is measured WITHOUT calling the LLM (free and fast):
# for each question we write a keyword that must appear in the correct chunk,
# then check if any of the top-k chunks contains it  ->  "hit rate".
# Fill eval_set from the real content of water_doc.pdf.
eval_set = [
    ("Where does groundwater come from?",               "aquifers"),
    ("What are the different sources of water?",        "rainwater"),
    ("How is water delivered to homes and farms?",      "canals"),
    ("What parameters are used to check water safety?", "turbidity"),
    ("Which technologies help find pipe leaks?",        "acoustic"),
    ("What is the overall goal of water management?",   "sustainability"),
]

def build_pipeline(chunk_size, overlap, model_name):
    model = SentenceTransformer(model_name)
    chs = chunk_pages(pages, chunk_size=chunk_size, overlap=overlap)
    emb = model.encode([c["text"] for c in chs], normalize_embeddings=True).astype("float32")
    idx = faiss.IndexFlatIP(emb.shape[1])
    idx.add(emb)
    return model, chs, idx


def hit_rate(model, chs, idx, k):
    hits = 0
    for question, keyword in eval_set:
        retrieved = search(question, k=k, index=idx, chunks=chs, model=model)
        if any(keyword.lower() in r["text"].lower() for r in retrieved):
            hits += 1
    return hits / len(eval_set)


results = []
for model_name in ["all-MiniLM-L6-v2", "all-mpnet-base-v2"]:
    for chunk_size, overlap in [(15, 3), (25, 5), (40, 10)]:
        model, chs, idx = build_pipeline(chunk_size, overlap, model_name)
        for k in [1, 2, 3]:
            results.append({
                "model": model_name,
                "chunk_size": chunk_size,
                "overlap": overlap,
                "num_chunks": len(chs),
                "k": k,
                "hit_rate": hit_rate(model, chs, idx, k),
            })

results_df = pd.DataFrame(results).sort_values(
    ["hit_rate", "k", "chunk_size"], ascending=[False, True, True]
)
print(results_df.to_string(index=False))
print("\nBest setting:\n", results_df.iloc[0])
