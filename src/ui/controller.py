import tkinter as tk
from importlib.util import source_hash

from Uebersichtsbildschirm import create_uebersicht_frame
from Spieleinstellungen import create_spieleinstellungen_superhirn_frame  # Expliziter Import
from src.spiel.variante import Variante  # Variante-Klasse importieren



# Hauptfenster
root = tk.Tk()
root.title("Superhirn")
root.geometry("550x500")
root.resizable(False, False)

# Globale Variablen für die Frames
uebersicht_frame = None
spieleinstellungen_frame = None  # Jetzt hinzufügen

# Variable für die Variante
spielVariante = Variante.SUPERSUPER # Standardvariante

# Funktion zum Setzen der Variante (wird von der UI aufgerufen)
def set_variante(variante: Variante):
    global spielVariante
    spielVariante = variante
    print(f"Variante gesetzt auf: {spielVariante}")  # Debug-Ausgabe
    print(spielVariante.steckplaetze)

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
        show_uebersicht,  # Zurück-Button-Callback
        spielVariante.steckplaetze,
        spielVariante
    )
    spieleinstellungen_frame.pack(fill="both", expand=True)

def show_uebersicht():
    global spieleinstellungen_frame, uebersicht_frame
    if spieleinstellungen_frame:
        spieleinstellungen_frame.pack_forget()
    if not uebersicht_frame:
        uebersicht_frame = create_uebersicht_frame(
        root,
        show_spieleinstellungen,
        set_variante
        )
    uebersicht_frame.pack(fill="both", expand=True)

# Starte mit der Übersicht
show_uebersicht()

root.mainloop()
