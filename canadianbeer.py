# Liabarys importieren
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
print(df.groupby("isAmericanStyle")[["score", "rank"]].mean().round(2))
print("---")

# PLOTS
plt.figure()
plt.pie(df["isAmericanStyle"].value_counts(), autopct="%1.0f%%", colors = ["lightblue", "grey"])
plt.title("Verteilung amerikanischer Biere mit nicht amerikanischen Bieren")
plt.legend(title = "Bierart", labels = ["american", "not american"])
# plt.show()
plt.close()

# Frage 6
print("Frage 6):")
print("---")

# Neue Variable: Ale / Stout / Other
df["beerType"] = np.where(
    df["style"].str.contains("Stout", case=False),
    "Stout",
    np.where(df["style"].str.contains("Ale", case=False), "Ale", "Other"),
)

ale_stout = df[df["beerType"].isin(["Ale", "Stout"])]

print("Anzahl Ale- und Stout-Biere:")
print(ale_stout["beerType"].value_counts())
print()

print("Mittelwerte von Score, Alkoholgehalt, Rank und Ratings nach Biertyp:")
print(ale_stout.groupby("beerType")[["score", "abv", "rank", "ratings"]].mean().round(2))
print("---")

# Plots: Score- und Alkoholvergleich Ale vs Stout
plt.figure()
sns.boxplot(data=ale_stout, x="beerType", y="score")
plt.title("Score von Ale- und Stout-Bieren")
plt.xlabel("Biertyp")
plt.ylabel("Score")
plt.grid(True, axis="y")
# plt.show()
plt.close()

plt.figure()
sns.boxplot(data=ale_stout, x="beerType", y="abv")
plt.title("Alkoholgehalt von Ale- und Stout-Bieren")
plt.xlabel("Biertyp")
plt.ylabel("Alkohol in %")
plt.grid(True, axis="y")
# plt.show()
plt.close()


# Frage 7
print("Frage 7):")
print("---")

corr_rank_score = df["rank"].corr(df["score"])
corr_rank_abv = df["rank"].corr(df["abv"])

print(f"Korrelationskoeffizient zwischen Rank und Score: {corr_rank_score:.2f}")
print(f"Korrelationskoeffizient zwischen Rank und Alkoholgehalt (abv): {corr_rank_abv:.2f}")
print("---")

# Scatterplots: Rank vs Score und Rank vs Alkoholgehalt
plt.figure()
sns.scatterplot(data=df, x="score", y="rank")
plt.title("Ranking in Abhängigkeit vom Score")
plt.xlabel("Score")
plt.ylabel("Rank")
plt.grid(True)
plt.gca().invert_yaxis()  # Rank 1 oben weil besser
# plt.show()
plt.close()

plt.figure()
sns.scatterplot(data=df, x="abv", y="rank")
plt.title("Ranking in Abhängigkeit von Alkoholgehalt")
plt.xlabel("Alkohol in % (abv)")
plt.ylabel("Rank")
plt.grid(True)
plt.gca().invert_yaxis()
# plt.show()
plt.close()


# Frage 8
print("Frage 8):")
print("---")

numeric_cols = ["score", "abv", "ratings", "rank"]
print("Korrelationsmatrix der numerischen Variablen:")
print(df[numeric_cols].corr().round(2))
print("---")

# Score vs Alkoholgehalt
plt.figure()
sns.scatterplot(data=df, x="abv", y="score")
plt.title("Score in Abhängigkeit vom Alkoholgehalt")
plt.xlabel("Alkohol in % (abv)")
plt.ylabel("Score")
plt.grid(True)
# plt.show()
plt.close()

# Score vs Anzahl Ratings
plt.figure()
sns.scatterplot(data=df, x="ratings", y="score")
plt.title("Score in Abhängigkeit von der Anzahl Ratings")
plt.xlabel("Anzahl Ratings")
plt.ylabel("Score")
plt.grid(True)
# plt.show()
plt.close()

# Score nach Bierstil (Top 5 häufigste Styles)
top_styles = df["style"].value_counts().head(5).index
df_top_styles = df[df["style"].isin(top_styles)]

plt.figure()
sns.boxplot(data=df_top_styles, x="style", y="score")
plt.title("Score nach Bierstil (Top 5 häufigste Stile)")
plt.xlabel("Style")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.grid(True, axis="y")
plt.tight_layout()
# plt.show()
plt.close() 
