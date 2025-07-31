import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

headers = ["a", "b", "c"]
df = pd.read_csv("Pythagorean_triples.csv", header=None, names=headers)
df.plot(x="a", y="b", style=".")
plt.show()
