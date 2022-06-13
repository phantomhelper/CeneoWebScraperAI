import os
import sys
import numpy as np
import pandas as pd
from opcode import opname
from fileinput import filename
from numpy import average, product
from matplotlib import pyplot as plt
print("-"*7)
print(*[filename.split(".")[0] for filename in os.listdir("./opinions/")], sep="\n")
print("-"*7)

product_id = str(sys.argv[1])

# product_id = input('Please enter a product\'s id: ')


opinions = pd.read_json(f"opinions/{product_id}.json")
if not os.path.exists("plots"):
    os.makedirs("plots")

opinions_count = len(opinions)
pros_count = opinions["pros"].map(bool).sum()
cons_count = opinions["cons"].map(bool).sum()
average_score = opinions["score"].mean().round(2)

stars_recommendation = pd.crosstab(opinions["rcmd"], opinions["score"], dropna=False)

recommendation = opinions["rcmd"].value_counts(dropna=False).sort_index().reindex([False, True, None])
print(opinions_count)
print(type(recommendation))
print(recommendation)
recommendation.plot.pie(
    label = "",
    title = "Recommendations: " + product_id,
    labels =["Not recommend", "Recommend", "No opinion"],
    colors = ["crimson", "forestgreen", "gray"],
    autopct = lambda p: f"{p:.1f}%".format(p) if p>0 else ""
)
plt.savefig(f"plots/{product_id}_rcmd.png")
plt.close()

stars = opinions["score"].value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
stars.plot.bar(
color = "hotpink"
)
plt.title("Opinions")
plt.xlabel("Count of Stars")
plt.ylabel("Count of opinions")
plt.grid(True, axis="y")
plt.xticks(rotation=0)
plt.savefig(f"plots/{product_id}_stars.png")
plt.close()