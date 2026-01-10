import tkinter as tk
from typing import List

from anwendung import spielengine, spielstart
from anwendung.spielstart import Spielstarter
from src.spiel.farbe import Farbe
from anwendung.modus import Modus
from src.anwendung.spielparameter import Spielparameter
from src.spiel.variante import Variante
from src.ui.sprache import Sprache
from src.spiel.spielCodes import Code
from ui.sichtbarkeiten import Sichtbarkeiten

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
spielAlgorithmus = "knuth"
spielSprache = Sprache.DEUTSCH
spielcode = None
spielZeit = None

# --- Funktionen zum Setzen der Parameter ---
def set_variante(variante: Variante):
    global spielVariante
    spielVariante = variante

def set_modus(modus: Modus):
    global spielModus, spieleinstellungen_frame
    spielModus = modus
    # print(f"Modus geändert auf: {modus}")                         # Debug

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

    if uebersicht_frame:
        uebersicht_frame.pack_forget()

    if spieleinstellungen_frame:
        spieleinstellungen_frame.destroy()

    sichtbarkeiten = Sichtbarkeiten.get_sichtbarkeit(spielModus)

    from Spieleinstellungen import create_spieleinstellungen_superhirn_frame
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
"""
    beim ausführen von spiel Starten Button soll 
    1. Spieloberfläche erzeugt werden und Spielstart erzeugt werden -> danach wird ein EngineInt zurückgegeben

"""



def on_code_spiel_start(code: Code, zeit: int):
    global spieloberflaeche_frame

    spielparameter = Spielparameter(
        variante=spielVariante,
        modus=spielModus,
        algorithmus=spielAlgorithmus if spielModus == Modus.M_C else None,
        delay=zeit,
        code=code
    )

    # Debug-Ausgabe
    print("\n--- Spielparameter ---")
    print(f"Variante: {spielparameter.variante.name}")
    print(f"Modus: {spielparameter.modus.name}")
    print(f"der Codierer ist {spielparameter.modus.codierer}")
    print(f"Algorithmus: {spielparameter.algorithmus}")
    print(f"Verzögerung: {spielparameter.delay} Sekunden")
    if code is not None:
        print("SpielCode:", [f.name for f in code.farben])                   # gibt das jeweilige Element aus .name aus der ENUM
    else:
        print("Code: None")
    print("-------------------------------")

    # Spiel starten und Engine-Objekt erhalten
    starter = Spielstarter()
    spiel_engine = starter.starteSpiel(spielparameter)

    """
    Mensch ist Codierer
        -> empfangen von rateversuch und feedback
        und Ausgabe in der spieloberfläche 
    """

    def rateversuch_erhalten_mensch_Codierer():
        feedback = spiel_engine.fuehreZugAus(None)

        letzte_runde = spiel_engine.spiel.runden[-1]

        zeile = letzte_runde.rundenNr - 1
        zeige_feedback(zeile, feedback)

        if spiel_engine.istFertig():
            print("Spiel beendet")

    def auto_raten():
        if not spiel_engine.istFertig():
            rateversuch_erhalten_mensch_Codierer()
            root.after(spielparameter.delay * 1000, auto_raten)

    """
    Einziger Callback: Empfängt den Rateversuch vom GUI
        Wird aufgerufen, wenn der Spieler einen Versuch bestätigt.
        farb_versuch wird an Spiel übergeben und feedback wird dann gespeichert 
    """
    def on_rateversuch_erhalten_menschRater(versuch: List[str], zeile: int):
        # print(f"\n--- Rateversuch (Zeile {zeile + 1}) ---")


        farb_versuch = Code([Farbe[farbe] for farbe in versuch])

        farb_namen = [f.name for f in farb_versuch.farben]
        print(f"Farben des Rateversuchs : {farb_namen}")

        feedback = spiel_engine.fuehreZugAus(farb_versuch)
        print(f"Feedback: {feedback.schwarz} schwarz, {feedback.weiss} weiß")
        zeige_feedback(zeile, feedback)


        if spiel_engine.istFertig():
            print("Spiel beendet")

    # Controller wird NICHT gebraucht (wir nutzen nur den Callback direkt)
    if spieleinstellungen_frame:
        spieleinstellungen_frame.pack_forget()

    from spieloberfläche import create_spieloberfläche
    if spieloberflaeche_frame:
        spieloberflaeche_frame.destroy()

    spieloberflaeche_frame, zeige_feedback = create_spieloberfläche(
        root,
        spielparameter,
        on_rateversuch_erhalten_menschRater,  # Einziger Callback: Übermittelt den Versuch an den Controller
        spielModus
    )
    spieloberflaeche_frame.pack(fill="both", expand=True)

    if spielModus.codierer == "mensch":
        auto_raten()

show_uebersicht()
root.mainloop()