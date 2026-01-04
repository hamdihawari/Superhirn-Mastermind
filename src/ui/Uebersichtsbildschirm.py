import tkinter as tk

from src.anwendung.modus import Modus
from src.spiel.variante import Variante
from src.ui.sprache import Sprache

def create_uebersicht_frame(root, next_callback, set_variante_callback, set_modus_callback,set_sprache_callback, sprache ):
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    # 1. Header-Frame für Überschrift + Kreise
    header_frame = tk.Frame(frame)
    header_frame.pack(fill="x", pady=10)

    # Überschrift (links im header_frame)
    ueberschrift_Label = tk.Label(
        header_frame,
        text=sprache.ueberschrift,
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
        text=sprache.variante_auswaehlen,
        font=("Arial", 22),
        bg="green"
    )
    ueberschrift_Variante.pack(anchor="w", pady=(0, 10))


    # ------------------------ Variantenauswahl : DYNAMISCHE VARIANTEN-LISTE AUS ENUM ---------------------------

    variante_namen = {                                                                      # Mapping von Variante-Enum zu Anzeigenamen
        Variante.SUPER: "Superhirn",
        Variante.SUPERSUPER: "Super-Superhirn"
    }

    # Variable, um die Auswahl zu speichern (StringVar, da wir Text-Werte haben)
    variante_auswahl = tk.StringVar(value="Superhirn")                                      # Standardwert & aktuelle ausgewählte Variable

    # Callback-Funktion, die bei Änderung der Auswahl aufgerufen wird
    def on_variante_change(*args):
        # Mapping von Anzeigenamen zurück zum Enum-Wert
        name_to_enum = {v: k for k, v in variante_namen.items()}
        selected_enum = name_to_enum[variante_auswahl.get()]                                # aktuelle Wert der Radiobuttons
        set_variante_callback(selected_enum)                                                # Enum-Wert an Controller übergeben

    variante_auswahl.trace_add("write", on_variante_change)                           #  StringVar mit Callback verknüpfen (wird bei Änderung aufgerufen)

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

    # ------------------------ Variantenauswahl : DYNAMISCHE VARIANTEN-LISTE AUS ENUM ---------------------------

    # ------------------------ Modus-Auswahl  ------------------------------
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
        text=sprache.modus_auswaehlen,
        font=("Arial", 22),
        bg="green"
    )
    ueberschrift_Modus.pack(anchor="w", padx=10)

    modus_namen = {                                                             # Mapping von den Anzeigenamen zu Modus-Enum
        Modus.M_C: Modus.M_C.description,
        Modus.C_M: Modus.C_M.description,
        Modus.C_C: Modus.C_C.description
    }

    modus_auswahl = tk.StringVar(value=Modus.M_C.description)                   # Standard ist Mensch der Codierer

    def on_modus_change(*args):
        name_to_enum = {v: k for k, v in modus_namen.items()}
        selected_enum = name_to_enum[modus_auswahl.get()]                       # Ausgewählten Namen aus modus_auswahl holen --> modus_auswahl.get() → Gibt den aktuell ausgewählten Anzeigenamen zurück (z. B. "Rater (C-M)").
        set_modus_callback(selected_enum)

    modus_auswahl.trace_add("write", on_modus_change)                         # beobachtet nur Änderungen und ruft die Callback-Funktion auf

    for modus_enum, anzeige_name in modus_namen.items():
        radiobutton = tk.Radiobutton(
            center_frame_Modus,
            text=anzeige_name,
            variable=modus_auswahl,
            value=anzeige_name,
            font=("Arial", 14),
            bg="green"
        )
        radiobutton.pack(side="left", padx=5, pady=10)


    # ------------------------ Modus-Auswahl  ------------------------------

    # ------------------------------ Frame für die Auswahl der Sprache und Button zum Bestätigen ------------------------------

    center_frame_Sprache = tk.Frame(frame, bg="green", borderwidth=5, padx=10, pady=10)
    center_frame_Sprache.pack(fill="x", padx=10, pady=2)

    ueberschrift_Sprache = tk.Label(
        center_frame_Sprache,
        text=sprache.sprache_auswaehlen,  # Dynamischer Text
        font=("Arial", 22),
        bg="green"
    )
    ueberschrift_Sprache.pack(anchor="w", padx=10)

    # Mapping von Sprache-Enum zu Anzeigenamen (description)
    sprache_namen = {
        Sprache.DEUTSCH: Sprache.DEUTSCH.description,
        Sprache.ENGLISCH: Sprache.ENGLISCH.description
    }

    sprache_auswahl = tk.StringVar(value=sprache.description)  # Standard: aktuelle Sprache

    def on_sprache_change(*args):
        name_to_enum = {v: k for k, v in sprache_namen.items()}
        selected_enum = name_to_enum[sprache_auswahl.get()]
        set_sprache_callback(selected_enum)

    sprache_auswahl.trace_add("write", on_sprache_change)

    for sprache_enum, anzeige_name in sprache_namen.items():
        radiobutton = tk.Radiobutton(
            center_frame_Sprache,
            text=anzeige_name,
            variable=sprache_auswahl,
            value=anzeige_name,
            font=("Arial", 14),
            bg="green"
        )
        radiobutton.pack(side="left", padx=25, pady=(0, 10))

    # --- Bestätigen-Button ---
    end_frame = tk.Frame(frame,borderwidth=5, padx=10, pady=10)
    end_frame.pack(fill="x", padx=10, pady=2)

    bestaetigenButton = tk.Button(
        end_frame,
        text=sprache.bestaetigen,  # Dynamischer Text
        command=next_callback,
        font=("Arial", 14, "bold"),
        bg="darkgreen",
        borderwidth=5,
        padx=10,
        pady=2
    )
    bestaetigenButton.pack(pady=10)
    return frame
