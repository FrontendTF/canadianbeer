# Liabarys importieren
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import statsmodels
import ISLP

# Markus

df = pd.read_csv("canadian_beers.csv")

# Frage 3
print("Frage 3):")
print("---")
listColumns = ["rank", "abv", "score", "ratings"]
print(f"{df[listColumns].describe().round(2)}\n")

for _ in listColumns:
    print(f"Varianz von {_}: {df[_].var().round(2)}")
print("---")

# PLOTS
plt.figure()
sns.boxplot(df["score"])
plt.title("Score von 100 Bieren")
plt.ylabel("Score")
plt.grid(True)
# plt.show()
plt.close()

plt.figure()
sns.boxplot(df["abv"])
plt.title("Alkoholgehalt von 100 Bieren")
plt.ylabel("Alkohol in %")
plt.grid(True)
# plt.show()
plt.close()

# Frage 4
print("Frage 4):")
print("---")
top3Styles = df["style"].value_counts().head(3).index
top3Breweries = df["brewery"].value_counts().head(3).index
top3StylesAndBreweries = df[df["brewery"].isin(top3Breweries) & df["style"].isin(top3Styles)]
print(top3StylesAndBreweries.groupby(["brewery", "style"])[["score", "rank"]].mean().round(2))
# PLOTS
plt.figure()
fig, axes = plt.subplots(2, 2, figsize = (14, 7))

sns.boxplot(data = top3StylesAndBreweries, x = "brewery", y = "score", hue = "brewery", ax = axes[0,0])
axes[0,0].set_title("Score-Verteilung der Top 3 Brauereien")
axes[0,0].set_xlabel("Brewery")
axes[0,0].set_ylabel("Score")
axes[0,0].grid(True, axis = "y")

sns.boxplot(data = top3StylesAndBreweries, x = "brewery", y = "rank", hue = "brewery", ax = axes[0,1])
axes[0,1].set_title("Rank-Verteilung der Top 3 Brauereien")
axes[0,1].set_xlabel("Brewery")
axes[0,1].set_ylabel("Rank")
axes[0,1].grid(True, axis = "y")

sns.boxplot(data = top3StylesAndBreweries, x = "style", y = "score", hue = "style", ax = axes[1,0])
axes[1,0].set_title("Score-Verteilung der Top 3 Bierarten")
axes[1,0].set_xlabel("Style")
axes[1,0].set_ylabel("Score")
axes[1,0].grid(True, axis = "y")

sns.boxplot(data = top3StylesAndBreweries, x = "style", y = "rank", hue = "style", ax = axes[1,1])
axes[1,1].set_title("Rank-Verteilung der Top 3 Bierarten")
axes[1,1].set_xlabel("Style")
axes[1,1].set_ylabel("Rank")
axes[1,1].grid(True, axis = "y")

plt.tight_layout()
# plt.show()
plt.close("all")

#groupSorted was just a test to try sort_values() on groupby(), its print is commented out. It is left in there for learning purposes.
"""
groupSorted = (
    top3Frame.groupby(["brewery", "style"])[["score", "rank"]]
    .mean()
    .round(2)
    .sort_values("score", ascending=False)
)
# print(groupSorted)
"""
print("---")

# QUESTION! Please leave it in here
"""
plt.figure()
barplotScoreSorted = df.sort_values("score")
sns.barplot(
    data = group,
    x="score",
    y="style",
    hue = "style"
)
plt.title("Bier-Style nach Score")
plt.xlabel("Style")
plt.xlim(left = df["score"].min())
plt.ylabel("Score")
plt.grid(True, axis = "x")
# plt.show()
plt.close()
"""

# Frage 5
print("Frage 5):")
print("---")
df["isAmericanStyle"] = df["style"].apply(lambda x: 1 if "American" in x else 0)
print(df.groupby("isAmericanStyle")[["score", "rank"]].mean().round(2).value_counts())
print("---")

# PLOTS
plt.figure()
plt.pie(df["isAmericanStyle"].value_counts(), autopct="%1.0f%%", colors = ["lightblue", "grey"])
plt.title("Verteilung amerikanischer Biere mit nicht amerikanischen Bieren")
plt.legend(title = "Bierart", labels = ["american", "not american"])
plt.show()
plt.close()

# Lukas


# Thomas
