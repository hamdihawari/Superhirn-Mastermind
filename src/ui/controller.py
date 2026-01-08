import tkinter as tk
from typing import List

from src.anwendung.modus import Modus
from src.anwendung.spielparameter import Spielparameter
from src.spiel.variante import Variante
from src.ui.sprache import Sprache
from src.spiel.spielCodes import Code

# Hauptfenster
root = tk.Tk()
root.title("Superhirn")
root.geometry("700x600")
root.resizable(False, False)

# Globale Variablen für die Frames
uebersicht_frame = None
spieleinstellungen_frame = None
spieloberflaeche_frame = None

# Standardwerte
spielVariante = Variante.SUPER
spielModus = Modus.M_C
spielAlgorithmus = "Knuth"
spielSprache = Sprache.DEUTSCH
spielcode = None
spielZeit = None

# --- Funktionen zum Setzen der Parameter ---
def set_variante(variante: Variante):
    global spielVariante
    spielVariante = variante


def set_modus(modus: Modus):
    global spielModus
    spielModus = modus


def set_sprache(sprache: Sprache):
    global spielSprache
    spielSprache = sprache


def set_algorithm(algorithm: str):
    global spielAlgorithmus
    spielAlgorithmus = algorithm


def set_code(code: Code):
    global spielcode
    spielcode = code


def set_zeit(zeit: int):
    global spielZeit
    spielZeit = zeit


# --- Frame-Wechsel-Funktionen ---
def show_uebersicht():
    global uebersicht_frame, spieleinstellungen_frame
    if spieleinstellungen_frame:
        spieleinstellungen_frame.pack_forget()
    if uebersicht_frame:
        uebersicht_frame.destroy()

    # Dynamischer Import (vermeidet zirkuläre Abhängigkeit)
    from Uebersichtsbildschirm import create_uebersicht_frame
    uebersicht_frame = create_uebersicht_frame(
        root,
        show_spieleinstellungen,
        set_variante,
        set_modus,
        set_sprache,
        spielSprache
    )
    uebersicht_frame.pack(fill="both", expand=True)

def show_spieleinstellungen():
    global spieleinstellungen_frame, uebersicht_frame

    # Prüfe, ob root noch existiert
    if not root.winfo_exists():
        print("Fehler: Hauptfenster wurde zerstört!")
        return

    if uebersicht_frame:
        uebersicht_frame.pack_forget()

    # Dynamischer Import
    from Spieleinstellungen import create_spieleinstellungen_superhirn_frame

    if spieleinstellungen_frame:
        spieleinstellungen_frame.destroy()

    # Erstelle das neue Frame
    spieleinstellungen_frame = create_spieleinstellungen_superhirn_frame(
        root,
        show_uebersicht,
        on_code_spiel_start,
        set_algorithm,
        spielVariante.steckplaetze,
        spielVariante,
        spielModus,
        spielSprache
    )
    spieleinstellungen_frame.pack(fill="both", expand=True)

# --- Haupt-Callback für Spielstart ---
def on_code_spiel_start(code: Code, zeit: int):
    global spieloberflaeche_frame

    spielparameter = Spielparameter(
        variante=spielVariante,
        modus=spielModus,
        algorithmus=spielAlgorithmus if spielModus == Modus.M_C else None,
        delay=zeit,
        code=code
    )

    # Einziger Callback: Empfängt den Rateversuch vom GUI
    def on_rateversuch_erhalten(versuch: List[str], zeile: int):
        """Wird aufgerufen, wenn der Spieler einen Versuch bestätigt.
        Args:
            versuch: Liste der Farben (z. B. ["ROT", "GRUEN", "BLAU", "GELB"])
            zeile: Aktuelle Zeile (0-9)
        """
        print(f"\n--- Rateversuch (Zeile {zeile + 1}) ---")
        print(f"Empfangener Versuch: {versuch}")
        # Hier könnte später die Bewertung stattfinden (aber noch nicht!)

    # Controller wird NICHT gebraucht (wir nutzen nur den Callback direkt)
    if spieleinstellungen_frame:
        spieleinstellungen_frame.pack_forget()

    from spieloberfläche import create_spieloberfläche
    if spieloberflaeche_frame:
        spieloberflaeche_frame.destroy()

    spieloberflaeche_frame = create_spieloberfläche(
        root,
        spielparameter,
        on_rateversuch_erhalten  # Einziger Callback: Übermittelt den Versuch an den Controller
    )
    spieloberflaeche_frame.pack(fill="both", expand=True)

show_uebersicht()
root.mainloop()