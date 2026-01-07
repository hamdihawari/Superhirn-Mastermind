import tkinter as tk
from tkinter import Canvas, StringVar, OptionMenu

def create_spieloberfläche(root, spielparameter):
    frame = tk.Frame(root, bg="#D2B48C")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Canvas für das Spielfeld
    canvas = Canvas(frame, width=375, height=500, bg="#8B4513", bd=0, highlightthickness=0)
    canvas.pack(side="left", padx=10, pady=20)

    # Farben aus der Variante extrahieren
    farben = [farbe.name for farbe in spielparameter.variante.erlaubteFarben]
    farb_zuordnung = {
        "ROT": "red", "GRUEN": "green", "BLAU": "blue", "GELB": "yellow",
        "ORANGE": "orange", "BRAUN": "brown", "WEISS": "white", "SCHWARZ": "black"
    }

    # Dropdown für Farbauswahl
    farbauswahl_var = StringVar(frame)
    farbauswahl_var.set(farben[0])  # Standardfarbe

    dropdown_frame = tk.Frame(frame, bg="#D2B48C")
    dropdown_frame.pack(pady=5)
    tk.Label(dropdown_frame, text="Aktuelle Farbe:", bg="#D2B48C").pack(side=tk.LEFT)
    dropdown = OptionMenu(dropdown_frame, farbauswahl_var, *farben)
    dropdown.config(bg="#D2B48C")
    dropdown.pack(side=tk.LEFT, padx=5)

    # NUR DIE ERSTE ZEILE wird bearbeitbar gemacht
    steine = {}
    for spalte in range(spielparameter.variante.steckplaetze):
        id = canvas.create_oval(
            30 + spalte * 40,
            80,  # Nur erste Zeile (Y-Position fest)
            50 + spalte * 40,
            100,
            fill="gray50",
            outline="black",
            tags=f"stein_0_{spalte}"  # Zeile 0
        )
        steine[spalte] = id  # Speichere nur die erste Zeile
        canvas.tag_bind(id, "<Button-1>",
                      lambda e, s=spalte, f=farbauswahl_var, c=canvas, st=steine:
                          setze_stein(c, s, farb_zuordnung[f.get()], st))

    # Bewertungskreise (leer, da noch nicht bewertet)
    for i in range(4):  # 4 Bewertungsfelder (2 schwarze, 2 weiße)
        canvas.create_oval(
            190 + (i % 2) * 20, 85 + (i // 2) * 15,
            200 + (i % 2) * 20, 95 + (i // 2) * 15,
            fill="gray80", outline="black"
        )

    # Button zum Ausgeben der Farbkombination im Terminal
    def ausgabe_im_terminal():
        versuch = []
        for spalte in range(spielparameter.variante.steckplaetze):
            farbe = canvas.itemcget(steine[spalte], "fill")
            # Umkehrung der farb_zuordnung für die Ausgabe (z. B. "red" → "ROT")
            farbe_name = [k for k, v in farb_zuordnung.items() if v == farbe][0]
            versuch.append(farbe_name)
        print("\n--- Rateversuch (Zeile 1) ---")
        print(f"Farbkombination: {versuch}")

    def setze_stein(canvas, spalte, farbe, steine):
        canvas.itemconfig(steine[spalte], fill=farbe)

    ausgabe_button = tk.Button(
        frame,
        text="Kombination ausgeben",
        command=ausgabe_im_terminal,
        bg="#8B4513",
        fg="white",
        font=("Arial", 12, "bold")
    )
    ausgabe_button.pack(pady=10)

    return frame
