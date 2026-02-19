# Superhirn (Mastermind)

Projekt im Rahmen des Moduls **Software Engineering II** (HTW Berlin).  
**Superhirn** ist eine erweiterbare Mastermind-Implementierung mit mehreren Spielmodi (lokal & optional online) und einer klaren Schichtenarchitektur.

---

## Überblick

Bei Superhirn muss ein Geheimcode aus Farben erraten werden. Jeder Rateversuch wird mit Feedback bewertet:

- **Schwarz**: richtige Farbe am richtigen Platz
- **Weiß**: richtige Farbe am falschen Platz

### Unterstützte Varianten

- **Superhirn**: 4 Steckplätze, 6 Farben
- **Super-Superhirn**: 5 Steckplätze, 8 Farben (inkl. Schwarz & Weiß)

---

## Spielmodi

- **Computer → Mensch (lokal)**: Computer erzeugt den Geheimcode, Mensch rät (max. 10 Runden)
- **Mensch → Computer (lokal)**: Mensch setzt Geheimcode, Computer rät mittels Algorithmus (optional mit Delay)
- **Computer → Computer (lokal / Beobachtung)**: Beide Rollen Computer; Mensch beobachtet und wählt Algorithmus
- **Mensch → Computer VS (lokal)**: Zwei Algorithmen raten parallel gegen denselben vom Menschen gesetzten Code
- **Computer → Mensch (online)**: Externer Server ist Codierer; Client sendet Züge per HTTP/JSON und erhält Feedback
- **Computer → Computer (online)**: Externer Server ist Codierer; lokaler Algorithmus rät über HTTP/JSON

---

## Architektur (Schichtenmodell)

Das System folgt einer klaren Schichtenarchitektur; jede Schicht kommuniziert nur mit benachbarten Schichten:

1. **UI-Layer**: Darstellung & Eingaben (keine Spiellogik)
2. **Anwendungs-Layer**: Orchestrierung/Steuerung, Spielinitialisierung, Modus-Ablauf
3. **Game-Layer**: fachlicher Kern (Spielregeln, Zustände, Feedback-Berechnung)
4. **Strategie/Player-Subsystem (Teil des Game-Layers)**: Spielerrollen + austauschbare Algorithmen
5. **Online-/Kommunikations-Layer (optional)**: HTTP/JSON-Kommunikation über definierte Schnittstelle

### Zentrale Designentscheidungen

- Strikte Trennung von Fachlogik und Technik (UI/HTTP unabhängig vom Game-Layer)
- Algorithmen vollständig austauschbar (**Strategy Pattern**)
- Online-Funktionalität optional und modular integrierbar
- Gute Testbarkeit durch geringe Kopplung und klare Verantwortlichkeiten

---

## Algorithmen (Auswahl)

- **Knuth**: systematische Reduktion des Suchraums, effiziente Lösungsstrategie
- **Step-By-Step**: inkrementeller Ansatz (gut für Vergleich/Didaktik)

---

## UML

Die UML-Diagramme liegen unter:

- `docs/uml/` (z. B. `architecture.png`, `class-core.png`, `sequence-online.png`)
- optional zusätzlich als PlantUML-Quellen: `docs/uml/*.puml`

---

## Installation & Start

### Voraussetzungen

- Python **3.x** (empfohlen: virtuelles Environment)
- Abhängigkeiten:
  - `requests` (für Online-Modi)
  - `pytest` (Tests)
  - `responses` (Mocking der Server-Responses für Online-Tests)

### Setup (Beispiel)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install requests pytest responses

### Start

```bash
python src/ui/main.py