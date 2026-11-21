import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
MODEL = "qwen/qwen3.8-27b"

SNIPPETS = {
    "logic_bug": {
        "purpose": "Compute the average of a list of meter readings.",
        "code": '''def average_usage(readings):
    total = 0
    for i in range(1, len(readings)):
        total += readings[i]
    return total / len(readings)
''',
    },
    "security": {
        "purpose": "Get a meter record from the database by id.",
        "code": '''API_KEY = "sk-live-12345"

def get_meter(conn, meter_id):
    query = f"SELECT * FROM meters WHERE id = '{meter_id}'"
    return conn.execute(query).fetchall()
''',
    },
    "clean_code": {
        "purpose": "Read a text file and return its lines.",
        "code": '''def read_lines(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\\n") for line in f]
''',
    },
}

BASE_PROMPT = "Review the following Python code and suggest improvements.\n\n{code}"

ROLE = "You are a senior Python code reviewer. Explain issues simply for a junior developer."

RULES = """
Check: bugs, security, performance, readability.
Only report real issues. If the code is fine, say so.
Think step by step before giving the final review.
"""

FORMAT = """
For each issue write:
- Line:
- Severity: High / Medium / Low
- Problem:
- Fix:
End with a score out of 10.
"""

EXAMPLE = """
Example:
Code: def ratio(a, b): return a / b
Review:
- Line: 1
- Severity: High
- Problem: Crashes when b is 0.
- Fix: Check if b == 0 before dividing.
Score: 6/10
"""

ENHANCED_USER = """Purpose of the code: {purpose}

<code>
{code}
</code>"""

EXPERIMENTS = {
    "1_base": {"system": None, "user": BASE_PROMPT},
    "2_enhanced": {"system": ROLE + RULES + FORMAT + EXAMPLE, "user": ENHANCED_USER},
    "3_no_example": {"system": ROLE + RULES + FORMAT, "user": ENHANCED_USER},
}


def review(system, user):
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": user})
    response = client.chat.completions.create(model=MODEL, messages=messages, temperature=0.2,max_tokens=900)
    return response.choices[0].message.content


output = []
for exp_name, exp in EXPERIMENTS.items():
    for snip_name, snip in SNIPPETS.items():
        user = exp["user"].format(code=snip["code"], purpose=snip["purpose"])
        print(f"Running {exp_name} on {snip_name} ...")
        answer = review(exp["system"], user)
        output.append(f"# {exp_name} / {snip_name}\n\n{answer}\n")

with open("results.md", "w", encoding="utf-8") as f:
    f.write("\n---\n\n".join(output))

print("Done. Open results.md")
