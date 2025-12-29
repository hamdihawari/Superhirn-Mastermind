import tkinter as tk
from src.spiel.variante import Variante

def create_uebersicht_frame(root, next_callback, set_variante_callback):
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True) # WICHTIG: Frame füllt das Fenster aus!

    # 1. Header-Frame für Überschrift + Kreise
    header_frame = tk.Frame(frame)
    header_frame.pack(fill="x", pady=10)  # Füllt die Breite aus

    # Überschrift (links im header_frame)
    ueberschrift_Label = tk.Label(
        header_frame,
        text="Superhirn - Übersicht",
        fg="green",
        font=("Arial", 30, "underline")
    )
    ueberschrift_Label.pack(side="left")

    # Kreise (rechts neben der Überschrift)
    for farbe in ["red", "green", "blue", "orange"]:
        kreis = tk.Label(
            header_frame,
            text="●",
            fg=farbe,
            font=("Arial", 36)
        )
        kreis.pack(side="left", padx=2)

    # --- Frame für die Auswahl der Checkboxen der Varianten ---

    center_frame_Variante = tk.Frame(
        frame,
        bg="green",
        borderwidth=5,
        padx=10,
        pady=10
    )
    center_frame_Variante.pack(fill="x", padx=10, pady=2)

    # Überschrift "Variante auswählen:"
    ueberschrift_Variante = tk.Label(
        center_frame_Variante,
        text="Variante auswählen :",
        font=("Arial", 22),
        bg="green"
    )
    ueberschrift_Variante.pack(anchor="w", pady=(0, 10))






    # --- DYNAMISCHE VARIANTEN-LISTE AUS ENUM ---
    # Mapping von Variante-Enum zu Anzeigenamen
    variante_namen = {
        Variante.SUPER: "Superhirn",
        Variante.SUPERSUPER: "Super-Superhirn"
    }

    # Variable, um die Auswahl zu speichern (StringVar, da wir Text-Werte haben)
    variante_auswahl = tk.StringVar(value="Superhirn")  # Standardwert

    # Callback-Funktion, die bei Änderung der Auswahl aufgerufen wird
    def on_variante_change(*args):
        # Mapping von Anzeigenamen zurück zum Enum-Wert
        name_to_enum = {v: k for k, v in variante_namen.items()}
        selected_enum = name_to_enum[variante_auswahl.get()]
        set_variante_callback(selected_enum)  # Enum-Wert an Controller übergeben

    # StringVar mit Callback verknüpfen (wird bei Änderung aufgerufen)
    variante_auswahl.trace_add("write", on_variante_change)

    # Radiobuttons für jede Variante erstellen
    for variante_enum, anzeige_name in variante_namen.items():
        radiobutton = tk.Radiobutton(
            center_frame_Variante,
            text=anzeige_name,
            variable=variante_auswahl,
            value=anzeige_name,
            font=("Arial", 14),
            bg="green"
        )
        radiobutton.pack(side="left", padx=25, pady=(0, 10))







    # --- Frame für die Auswahl der Checkboxen des Modus ---
    center_frame_Modus = tk.Frame(
        frame,
        bg="green",
        borderwidth=5,  # Rahmenbreite in Pixeln
        padx=10,  # Innenabstand links/rechts
        pady=10  # Innenabstand oben/unten
    )
    center_frame_Modus.pack(fill="x", padx=10, pady=2)

    # Überschrift "Modus auswählen:"
    ueberschrift_Modus = tk.Label(
        center_frame_Modus,
        text="Modus auswählen :",
        font=("Arial", 22),
        bg="green"
    )

    ueberschrift_Modus.pack(anchor="w", pady=(0, 10))

    # Liste der Modi !! --> muss noch getter auf die ENUMs haben
    Modi = ["Codierer (M-C)", "Rater (C-M)", "Zuschauer (C-C)"]

    modi_auswahl = tk.StringVar(value="Codierer (M-C)")

    for modi in Modi:
        radiobutton = tk.Radiobutton(
            center_frame_Modus,
            text=modi,
            variable=modi_auswahl,
            value=modi, font=("Arial", 14),
            bg="green"
        )
        radiobutton.pack(side="left", padx=5, pady=(0, 10))

    # --- Frame für die Auswahl der Sprache und Button zum Bestätigen---

    end_frame_Modus = tk.Frame(
        frame,
        bg="green",
        borderwidth=5,  # Rahmenbreite in Pixeln
        padx=10,  # Innenabstand links/rechts
        pady=10  # Innenabstand oben/unten
    )
    end_frame_Modus.pack(fill="x", padx=10, pady=2)

    sprachenListe = tk.Listbox(
        end_frame_Modus,
        font=("Arial", 8),
        bg="lightgreen",
        borderwidth=2,
    )
    sprachenListe.pack(side="left", padx=10, pady=10)

    # Sprachen hinzufügen
    sprachen = ["Deutsch", "Englisch"]
    for sprache in sprachen:
        sprachenListe.insert(tk.END, sprache)

    bestätigenButton = tk.Button(
        end_frame_Modus,
        text="Bestätigen",
        command=next_callback,
        font=("Arial", 14, "bold"),
        bg="darkgreen",
        borderwidth = 5,
        padx = 10,
        pady = 2
    )
    bestätigenButton.pack(side="left", padx=100, pady=10)

    return frame
