# %%
x = 10

# %%
print(x * 2)

# %%
import sys
import pandas as pd
import num as np

print("Python:", sys.version.split()[0])
print("Pandas:", pd.__version__)
print("NumPy:", np.__version__)
# %%
print("Hello")
# %%
import matplotlib.pyplot as plt

# %%
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
# %%
plt.bar([5, 9, 3], [5, 9, 3])
plt.title("Simple bar chart")
plt.show()
