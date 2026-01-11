import tkinter as tk
from typing import List, Callable
from tkinter import Canvas

from spiel.spielCodes import Code
from spiel.variante import Variante
from src.anwendung.spielparameter import Spielparameter
from src.spiel.variante import Farbe
from ui.sichtbarkeiten import Sichtbarkeiten



def create_spieloberfläche(
    root,
    spielparameter: Spielparameter,
    on_rateversuch_erhalten: Callable,  # Einziger Callback: Sendet Rateversuch an Controller
    spielmodus
):
    sichtbarkeiten = Sichtbarkeiten.get_sichtbarkeit(spielmodus)

    # Hauptframe
    frame = tk.Frame(root, bg="#D2B48C")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # --- Spielfeld (links) ---
    canvas = Canvas(frame, width=375, height=500, bg="#8B4513", bd=0, highlightthickness=0)
    canvas.pack(side="left", padx=10, pady=20)

    # --- Steuerung (rechts) ---
    steuerungs_frame = tk.Frame(frame, bg="#D2B48C")
    steuerungs_frame.pack(side="right", fill="y", padx=10, pady=10)




    # Farben und Zuordnung
    farben = [farbe.name for farbe in spielparameter.variante.erlaubteFarben]
    farb_zuordnung = {
        "ROT": "red", "GRUEN": "green", "BLAU": "blue", "GELB": "yellow",
        "ORANGE": "orange", "BRAUN": "brown", "WEISS": "white", "SCHWARZ": "black"
    }
    farb_rückzuordnung = {v: k for k, v in farb_zuordnung.items()}

    # Aktuelle Zeile und Steine verwalten
    aktuelle_zeile = 0
    alle_zeilen = []

    # 10 Zeilen für das Spiel erstellen
    for zeile in range(10):
        steine = []
        feedback_steine = []

        # Rateversuch - Steckplätze
        for spalte in range(spielparameter.variante.steckplaetze):
            x = 50 + spalte * 50
            y = 50 + zeile * 40
            kreis = canvas.create_oval(x, y, x + 30, y + 30, fill="white", outline="black")
            steine.append(kreis)

        # Feedback - Steckplätze
        import math

        feedback_count = spielparameter.variante.steckplaetze
        cols = math.ceil(feedback_count / 2)

        for i in range(feedback_count):
            col = i % cols
            row = i // cols

            fx = (
                    50
                    + spielparameter.variante.steckplaetze * 50
                    + 20
                    + col * 15
            )
            fy = (
                    50
                    + zeile * 40
                    + row * 15
            )

            fb = canvas.create_oval(
                fx, fy,
                fx + 10, fy + 10,
                fill="gray",
                outline="black"
            )
            feedback_steine.append(fb)

        alle_zeilen.append({
            "steine": steine,
            "feedback": feedback_steine
        })

    fehler_label = tk.Label(
        steuerungs_frame,
        text="",
        fg="red",
        bg="#D2B48C",
        font=("Arial", 10, "bold")
    )
    fehler_label.pack(pady=5)

    def zeige_fehlermeldung(nachricht: str):
        fehler_label.config(text=nachricht)
        root.after(3000, lambda: fehler_label.config(text=""))  # Nach 3 Sekunden verschwindet die Meldung

    def zeige_runde_code(zeile: int, runde_code: Code):
        steine = alle_zeilen[zeile]["steine"]

        for spalte, farbe in enumerate(runde_code.farben):
            farbe_hex = farb_zuordnung[farbe.name]
            canvas.itemconfig(steine[spalte], fill=farbe_hex)

    def zeige_feedback(zeile: int, feedback):

        feedback_steine = alle_zeilen[zeile]["feedback"]

        index = 0

        for _ in range(feedback.schwarz):
            canvas.itemconfig(feedback_steine[index], fill="black")
            index += 1

        for _ in range(feedback.weiss):
            canvas.itemconfig(feedback_steine[index], fill="white")
            index += 1


    """
    Mensch ist Rater -> dann zeige Farbauswahl an 
    """
    if sichtbarkeiten["show_code_auswahl_spiel_ui"]:
        farbauswahl_var = tk.StringVar(steuerungs_frame)
        farbauswahl_var.set(farben[0])
        dropdown = tk.OptionMenu(steuerungs_frame, farbauswahl_var, *farben)
        dropdown.config(bg="#D2B48C")
        dropdown.pack(pady=5)

        # Stein-Auswahl-Buttons (horizontal)
        stein_buttons_frame = tk.Frame(steuerungs_frame, bg="#D2B48C")
        stein_buttons_frame.pack(pady=5)

        def setze_farbe(spalte):
            farbe_name = farbauswahl_var.get()
            farbe_hex = farb_zuordnung[farbe_name]
            canvas.itemconfig(alle_zeilen[aktuelle_zeile]["steine"][spalte], fill=farbe_hex)

        for spalte in range(spielparameter.variante.steckplaetze):
            tk.Button(
                stein_buttons_frame,
                text=f"Stein {spalte + 1}",
                command=lambda s=spalte: setze_farbe(s),
                bg="#8B4513", fg="white"
            ).pack(side="left", padx=2)


    if sichtbarkeiten["show_code_auswahl_spiel_ui"]:
        """
        Rateversuch wird bestätigt und zurück an den controller gegeben --> dann an die Spiellogik
        Validierung: 
            - Wenn Superhirn Weiß als Farbe gewählt wird, dann soll einer Fehler ausgegeben werden 
        """
        def bestätige_rateversuch():
            nonlocal aktuelle_zeile
            versuch = []
            for spalte in range(spielparameter.variante.steckplaetze):
                farbe_hex = canvas.itemcget(alle_zeilen[aktuelle_zeile]["steine"][spalte], "fill")
                farbe_name = farb_rückzuordnung.get(farbe_hex, "WEISS")
                versuch.append(farbe_name)

            # --- VALIDIERUNG DIREKT IN DER GUI ---
            if "WEISS" in versuch and spielparameter.variante == Variante.SUPER:
                zeige_fehlermeldung("Keine weißen Steine übrig lassen.")
                return  # Abbrechen, Zeile wird NICHT erhöht

            erlaubte_farben = [f.name for f in spielparameter.variante.erlaubteFarben]
            for farbe in versuch:
                if farbe not in erlaubte_farben:
                    zeige_fehlermeldung(f"Die Farbe '{farbe}' ist nicht erlaubt!")
                    return  # Abbrechen, Zeile wird NICHT erhöht

            # --- NUR BEI GÜLTIGEM VERSUCH: WEITERMITTELN UND ZEILE ERHÖHEN ---
            on_rateversuch_erhalten(versuch, aktuelle_zeile)

            if aktuelle_zeile < 9:  # Nur erhöhen, wenn der Versuch gültig war
                aktuelle_zeile += 1

        tk.Button(
            steuerungs_frame,
            text="Rateversuch bestätigen",
            command=bestätige_rateversuch,
            bg="#4CAF50", fg="white",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

    return frame, zeige_feedback, zeige_runde_code, zeige_fehlermeldung
