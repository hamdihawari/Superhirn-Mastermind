import tkinter as tk
from Uebersichtsbildschirm import create_uebersicht_frame
from Spieleinstellungen import * # Jetzt importieren
from src.spiel.variante import Variante

# Hauptfenster
root = tk.Tk()
root.title("Superhirn")
root.geometry("550x500")
root.resizable(False, False)

# Globale Variablen für die Frames
uebersicht_frame = None
spieleinstellungen_frame = None  # Jetzt hinzufügen

# Variablen für die Variante
spielVariante: Variante | None = None                       # einen Wert vom Typ Variante (z. B. Variante.SUPER) oder None (also "leer") speichern.
spielVariante_test = Variante.SUPER                         # zum Testen ob Variante mit Super reagiert

def show_spieleinstellungen():
    global spieleinstellungen_frame, uebersicht_frame
    if uebersicht_frame:
        uebersicht_frame.pack_forget()
    if not spieleinstellungen_frame:
        # wenn Variante = Superhirn erstelle nur 4 Steckplätze mit den 6 Farben                 HIER WIRD GERADE GEARBEITET
        #create_spieleinstellungen_superhirn_frame(root, show_uebersicht())

        # wenn Variante = Super-Superhirn erstelle 5 Steckplätze mit den 8 Farben
        spieleinstellungen_frame = create_spieleinstellungen_frame(root, show_uebersicht)
    spieleinstellungen_frame.pack(fill="both", expand=True)

def show_uebersicht():
    global spieleinstellungen_frame, uebersicht_frame
    if spieleinstellungen_frame:
        spieleinstellungen_frame.pack_forget()
    if not uebersicht_frame:
        uebersicht_frame = create_uebersicht_frame(root, show_spieleinstellungen)  # Jetzt mit echten Callback
    uebersicht_frame.pack(fill="both", expand=True)

# Starte mit der Übersicht
show_uebersicht()

root.mainloop()
