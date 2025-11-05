# Auswertung - canadian_beers.csv 

# 1) & 2)
##  Aus welchen Beobachtungen setzen sich die Daten zusammen? Beschreiben Sie diese kurz und überlegen Sie sich, welches Skalenniveau die einzelnen Beobachtungen haben. & Wie setzen sich die einzelnen Beobachtungen zusammen? Verwenden Sie Methoden für univariate Datensätze sinnvoll.



| Variable | Skalenniveau | Methode                             | Beobachtung                                             |
| -------- | ------------ | ----------------------------------- | ------------------------------------------------------- |
| rank     | ordinal      | minimum, maximum, median            | rank, from 1 to 100, as rated by BeerAdvocate.com users |
| name     | nominal      | count                               | name of the beer                                        |
| brewery  | nominal      | count                               | the brewery responsible for this delicious creation     |
| style    | nominal      | count                               | the style of the beer                                   |
| abv      | Verhältnis   | average, mean, minimum, maximum, sd | Alcohol by Volume (%)                                   |
| score    | Intervall    | average, mean, minimun, maximum, sd | Overall score determined by BeerAdvocate.com users      |
| ratings  | Verhältnis   | average, mean, minimum, maximum, sd | Number of ratings                                       |

**Skalenniveau**: nominal (keine Rangordnung), ordinal (Rangfolge), Intervall (Gleichheit der Differenzen), Verhältnis (Wohldefinierter Nullpunkt)

# 3)
## Ermitteln Sie Kennzahlen für die einzelnen Beobachtungen, die Ihnen sinnvoll erscheinen. (Lokation, Modus, Varianzen, Quantile…)


# 4)
## Ermitteln Sie die 3 häufigsten Brauereien und Bier Arten, die in diesem Datensatz vorkommen. Wie verteilen sich Rang und Score auf diese Brauereien und Arten von Bier? Das Bier welcher Brauerei und welcher Art würden Sie jemandem empfehlen, wenn Sie sich nach dem Score richten? (Betrachten Sie hier nur die 3 häufigsten Arten)

# 5)
## Fügen Sie eine Variable ein, die anzeigt, ob es sich um ein american style beer handelt (Tipp: Variable style). Wie siehen scores und rank in diesem Fall aus?


