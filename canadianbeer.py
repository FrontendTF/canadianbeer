# Liabarys importieren
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import statsmodels
import ISLP

# TODO: pdf zum schluss gestalten

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

# Frage 4
print("Frage 4):")
print("---")
top3Styles = df["style"].value_counts().head(3).index
# print(top3Styles)

top3Frame = df[df["style"].isin(top3Styles)]
group = top3Frame.groupby(["brewery", "style"])[["score", "rank"]].mean().round(2)
print(group)

#groupSorted was just a test, its print is commented out. It is left in there for learning purposes.
groupSorted = (
    top3Frame.groupby(["brewery", "style"])[["score", "rank"]]
    .mean()
    .round(2)
    .sort_values("score", ascending=False)
)

# print(groupSorted)
print("---")

print("Frage 5):")
print("---")
df["isAmericanStyle"] = df["style"].apply(lambda x: 1 if "American" in x else 0)
print(df.groupby("isAmericanStyle")[["score", "rank"]].mean().round(2))
print("---")

# Lukas


# Thomas
