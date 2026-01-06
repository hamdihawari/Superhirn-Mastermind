import tkinter as tk
from importlib.util import source_hash

from Uebersichtsbildschirm import create_uebersicht_frame
from Spieleinstellungen import create_spieleinstellungen_superhirn_frame  # Expliziter Import
from spieloberfläche import create_spieloberfläche
from src.anwendung.modus import Modus
from src.spiel.variante import Variante  # Variante-Klasse importieren
from src.ui.sprache import Sprache
from src.spiel.spielCodes import Code

# Hauptfenster
root = tk.Tk()
root.title("Superhirn")
root.geometry("550x550")
root.resizable(False, False)

# Globale Variablen für die Frames
uebersicht_frame = None
spieleinstellungen_frame = None
spieloberflaeche_frame = None


spielVariante = Variante.SUPER          # Standardvariante
spielModus = Modus.M_C                  # Standardmodus
#spielAlgorithmus =                     # Mocking, danach dann
spielSprache = Sprache.DEUTSCH         # Standardsprache
spielcode = None

# Funktion zum Setzen der Variante (wird von der UI aufgerufen)
def set_variante(variante: Variante):
    global spielVariante
    spielVariante = variante
    print(f"Variante gesetzt auf: {spielVariante}")  # Debug-Ausgabe
    print(spielVariante.steckplaetze)

def set_modus(modus: str):
    global spielModus
    spielModus = modus
    print(f"Modus gesetzt auf: {modus.description}")

def set_sprache(sprache: Sprache):
    global spielSprache
    spielSprache = sprache
    print(f"Sprache gesetzt auf: {sprache.name}")

# Callback-Funktion für den "Bestätigen"-Button
def on_code_bestaetigt(code: Code):
    global spieloberflaeche_frame, spielcode
    set_code(code)

    if spieleinstellungen_frame:
        spieleinstellungen_frame.pack_forget()

    if spieloberflaeche_frame:
        spieloberflaeche_frame.destroy()

    # Übergabe der spielVariante an create_spieloberfläche
    spieloberflaeche_frame = create_spieloberfläche(root, spielVariante)
    spieloberflaeche_frame.pack(fill="both", expand=True)

def set_code(code: Code):
    global spielcode
    spielcode = code
    print(f"aktueller Code ist : {code.farben}")

def show_spieleinstellungen():
    global spieleinstellungen_frame, uebersicht_frame
    print(f"DEBUG: Aktuelle Variante: {spielVariante}, Steckplätze: {spielVariante.steckplaetze}")
    if uebersicht_frame:
        uebersicht_frame.pack_forget()
    # Frame NEU erstellen (auch wenn er schon existiert)
    if spieleinstellungen_frame:
        spieleinstellungen_frame.destroy()  # Alten Frame löschen
    spieleinstellungen_frame = create_spieleinstellungen_superhirn_frame(
        root,
        show_uebersicht,
        on_code_bestaetigt,
        spielVariante.steckplaetze,                                         # Anzahl an Steckplätze werden übergeben
        spielVariante,
        spielModus,
        spielSprache
    )
    spieleinstellungen_frame.pack(fill="both", expand=True)

def show_uebersicht():
    global spieleinstellungen_frame, uebersicht_frame

    if spieleinstellungen_frame:
        spieleinstellungen_frame.pack_forget()

    if uebersicht_frame:
        uebersicht_frame.destroy()

    uebersicht_frame = create_uebersicht_frame(
        root,
        show_spieleinstellungen,
        set_variante,
        set_modus,
        set_sprache,
        spielSprache
        )
    uebersicht_frame.pack(fill="both", expand=True)

# Starte mit der Übersicht
show_uebersicht()

root.mainloop()
