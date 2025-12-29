import tkinter as tk
from tkinter import ttk

from src.spiel.variante import Variante, Farbe

def create_spieleinstellungen_superhirn_frame(root, back_callback,anzahl_steckplaetze,spielVariante):


    frame = tk.Frame(root)


    farben = [farbe.name for farbe in spielVariante.erlaubteFarben]

    # --- Überschrift (oben) ---
    header_frame = tk.Frame(frame)
    header_frame.pack(anchor="nw", pady=10)

    tk.Label(
        header_frame,
        text="Einstellungen",
        fg="black",
        font=("Arial", 36, "underline")
    ).pack(side="left")

    # --- Hauptframe (grüner Bereich) für die Farbauswahl ---
    upperCenter_frame = tk.Frame(frame, bg="green", borderwidth=5, padx=10, pady=2)
    upperCenter_frame.pack(anchor="nw", fill="x", padx=10, pady=2)

    # Überschrift "Farbauswahl" im grünen Frame
    farbauswahl_label = tk.Label(
        upperCenter_frame,
        text="Farbauswahl",
        font=("Arial", 20, "bold"),
        bg="green"
    )
    farbauswahl_label.grid(row=0, column=0, columnspan=2, sticky="w")

    # Dynamische Erstellung der Steckplätze
    for i in range(1, anzahl_steckplaetze + 1):
        row = (i - 1) % 3  # Max. 3 Zeilen pro Spalte
        col = (i - 1) // 3  # Wechsel in die nächste Spalte nach 3 Zeilen

        block_frame = tk.Frame(upperCenter_frame, bg="green")
        block_frame.grid(row=row + 1, column=col, sticky="w", pady=5)

        nummer_label = tk.Label(
            block_frame,
            text=f"{i}",
            bg="lightgray",
            width=2,
            font=("Arial", 14)
        )
        nummer_label.pack(side="left", padx=5)

        farbe_var = tk.StringVar(value=farben[0])
        farbe_option = tk.OptionMenu(block_frame, farbe_var, *farben)
        farbe_option.config(bg="white", width=15, font=("Arial", 12))
        farbe_option.pack(side="left", padx=5)



    # --- Hauptframe für die Algorithmusauswahl--
    center_frame = tk.Frame(frame, bg="green", borderwidth=5, padx=10, pady=2)
    center_frame.pack(anchor="nw", padx=10, pady=2, fill="x")
    algorithmus_label = tk.Label()

    # Überschrift für Algorithmusauswahl
    algorithmus_label = tk.Label(
        center_frame,
        text="Algorithmus auswählen",
        fg="black",
        bg="green",
        font=("Arial", 14, "bold")
    )
    algorithmus_label.pack(anchor="nw", pady=2)

    algorithmen = ["Knuth", "Step-by-Step"]
    algorithmen_auswahl = tk.StringVar(value="Knuth")

    for algorithm in algorithmen:
        algorithm_radiobutton = tk.Radiobutton(
            center_frame,
            text=algorithm,
            variable=algorithmen_auswahl,
            value=algorithm,
            font=("Arial", 14, "bold"),
            bg="green"
        )
        algorithm_radiobutton.pack(side="left", padx=50, pady=2)

    # --- Hauptframe für die Zeitverzögerung--
    lower_frame = tk.Frame(frame, bg="green", borderwidth=5, padx=10, pady=2)
    lower_frame.pack(anchor="nw", padx=10, pady=2, fill="x")

    zeitverzögerungs_label = tk.Label(
        lower_frame,
        text="Zeitverzögerung der Maschine in sekunden ",
        fg="black",
        bg="green",
        font=("Arial", 14, "bold")
    )
    zeitverzögerungs_label.pack(anchor="nw", pady=2)

    zeiten = [1, 2, 3, 4, 5]

    zeiten_frame = tk.Frame(
        lower_frame,
        bg="green",
    )

    zeiten_frame.pack(side="left", padx=10, pady=2)

    zeit_var = tk.StringVar(value=zeiten[0])

    zeit_option = tk.OptionMenu(
        zeiten_frame,
        zeit_var,
        *zeiten
    )
    zeit_option.config(bg="white", width=15, font=("Arial", 12))
    zeit_option.pack(side="left", padx=5, pady=2)

    zurückButton_Spieleinstellungen = tk.Button(
        zeiten_frame,
        text="Zurück",
        command=back_callback,
        bg="green",
        font=("Arial", 14, "bold"),
        borderwidth=5,
        padx=10,
        pady=2,
    )
    zurückButton_Spieleinstellungen.pack(side="left", padx=20, pady=2)

    bestätigenButton = tk.Button(
        zeiten_frame,
        text = "Bestätigen",
        # command=                      # folge noch mit der Spielübersicht
        bg="green",
        font=("Arial", 14, "bold"),
        borderwidth=5,
        padx=10,
        pady=2
    )
    bestätigenButton.pack(side="left", padx=10, pady=2)

    return frame