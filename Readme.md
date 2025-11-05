# Canadianbeer

## Installation

### Wichtig

Für dieses Projekt wird Python 3.12 verwendet.
Die vorgegebenen Bibliotheken (requirements.txt Vorgaben von Müslüm Atlas) sind älter und stellen teils keine fertigen Wheels für Python 3.14 bereit.
Mit Python 3.12 lassen sich alle Pakete direkt über pip installieren, ohne zusätzliche Tools wie conda oder spezielle Build Tools. Sollten Sie zusätzliche libraries installieren wollen bitte über requirements.txt hinzufügen.

### Schritte

```powershell
# In den Projektordner wechseln
cd "C:\Users\...\Canadianbeer"

# alte venv löschen (falls vorhanden)
deactivate   # nur, falls eine Umgebung gerade aktiv ist
Remove-Item -Recurse -Force .venv

# neue venv mit Python 3.12 anlegen
py -3.12 -m venv .venv

# venv aktivieren
.\.venv\Scripts\Activate.ps1

# Version prüfen
python --version

# pip aktualisieren
python -m pip install --upgrade pip

# Abhängigkeiten installieren
pip install -r requirements.txt
```

### Plots bei Ausführung des Codes anzeigen lassen

Um Plots nach der Reihe automatisch anzuzeigen lassen müssen die:

```python
# plt.show()
```

Hashtags entfernt werden bei plt.show()

## Teammitglieder für Aufgabe 1

- Thomas Feyerl MSD
- Markus Rossman MSD
- Lucas Gregor Wychodil-Lubi MSD
