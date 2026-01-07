import tkinter as tk
from src.spiel.spielCodes import Code
from src.spiel.variante import Variante, Farbe

def create_spieleinstellungen_superhirn_frame(
    root,
    back_callback,
    spielstart_callback,  # ← on_code_spiel_start wird als Parameter übergeben
    set_algorithm_callback,
    anzahl_steckplaetze,
    spielVariante,
    spielmodus,
    sprache
):
    frame = tk.Frame(root)
    farbe_vars = []  # Speichert alle StringVars der OptionMenüs


    header_frame = tk.Frame(frame)
    header_frame.pack(anchor="nw", pady=10)

    tk.Label(
        header_frame,
        text=sprache.einstellungen,
        fg="black",
        font=("Arial", 36, "underline")
    ).pack(side="left")

    # Farbauswahl (falls spielmodus.show_farbe = True)
    if spielmodus.show_farbe:
        upperCenter_frame = tk.Frame(frame, bg="green", borderwidth=5, padx=10, pady=2)
        upperCenter_frame.pack(anchor="nw", fill="x", padx=10, pady=2)

        farbauswahl_label = tk.Label(
            upperCenter_frame,
            text=sprache.farbauswahl,
            font=("Arial", 20, "bold"),
            bg="green"
        )
        farbauswahl_label.grid(row=0, column=0, columnspan=2, sticky="w")

        farben = [farbe.name for farbe in spielVariante.erlaubteFarben]

        for i in range(1, anzahl_steckplaetze + 1):
            row = (i - 1) % 3
            col = (i - 1) // 3
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
            farbe_vars.append(farbe_var)
            farbe_option = tk.OptionMenu(block_frame, farbe_var, *farben)
            farbe_option.config(bg="white", width=15, font=("Arial", 12))
            farbe_option.pack(side="left", padx=5)

    # Algorithmusauswahl (falls spielmodus.show_algorithmus = True)
    if spielmodus.show_algorithmus:
        center_frame = tk.Frame(frame, bg="green", borderwidth=5, padx=10, pady=2)
        center_frame.pack(anchor="nw", padx=10, pady=2, fill="x")

        algorithmus_label = tk.Label(
            center_frame,
            text=sprache.algorithmus_auswaehlen,
            fg="black",
            bg="green",
            font=("Arial", 14, "bold")
        )
        algorithmus_label.pack(anchor="nw", pady=2)

        algorithmen = ["Knuth", "Step-by-Step"]
        algorithmen_auswahl = tk.StringVar(value="Knuth")

        def on_algorithm_auswahl_change(*args):
            selected_name = algorithmen_auswahl.get()
            set_algorithm_callback(selected_name)

        algorithmen_auswahl.trace_add("write", on_algorithm_auswahl_change)

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

    # Zeitverzögerung (falls spielmodus.show_zeit = True)
    if spielmodus.show_zeit:
        lower_frame = tk.Frame(frame, bg="green", borderwidth=5, padx=10, pady=2)
        lower_frame.pack(anchor="nw", padx=10, pady=2, fill="x")

        zeitverzögerungs_label = tk.Label(
            lower_frame,
            text=sprache.zeitverzoegerung,
            fg="black",
            bg="green",
            font=("Arial", 14, "bold")
        )
        zeitverzögerungs_label.pack(anchor="nw", pady=2)

        zeiten = [1, 2, 3, 4, 5]
        zeiten_frame = tk.Frame(lower_frame, bg="green")
        zeiten_frame.pack(side="left", padx=10, pady=2)

        zeit_var = tk.StringVar(value=zeiten[0])
        zeit_option = tk.OptionMenu(zeiten_frame, zeit_var, *zeiten)
        zeit_option.config(bg="white", width=15, font=("Arial", 12))
        zeit_option.pack(side="left", padx=5, pady=2)


    def on_spiel_start():
        # 1. Farbauswahl (immer vorhanden, wenn show_farbe=True)
        ausgewählte_farben = [farbe_var.get() for farbe_var in farbe_vars]
        code = Code(farben=[Farbe[farbe] for farbe in ausgewählte_farben])

        # 2. Zeitauswahl (nur abfragen, wenn show_zeit=True)
        ausgewählte_zeit = 0  # Standardwert, falls keine Zeitauswahl existiert
        if spielmodus.show_zeit:
            ausgewählte_zeit = int(zeit_var.get())  # Nur abfragen, wenn zeit_var existiert

        # 3. Spiel starten
        spielstart_callback(code, ausgewählte_zeit)

    zurückButton_Spieleinstellungen = tk.Button(
        header_frame,
        text=sprache.zurueck,
        command=back_callback,
        bg="green",
        font=("Arial", 14, "bold"),
        borderwidth=5,
        padx=10,
        pady=2,
    )
    zurückButton_Spieleinstellungen.pack(side="left", padx=20, pady=2)

    bestätigenButton = tk.Button(
        header_frame,
        text=sprache.starten,
        command=on_spiel_start,
        bg="green",
        font=("Arial", 14, "bold"),
        borderwidth=5,
        padx=10,
        pady=2
    )
    bestätigenButton.pack(side="right", padx=10, pady=2)

    return frame
