import tkinter as tk
from tkinter import Canvas, StringVar, OptionMenu

def create_spieloberfläche(root, spielVariante):
    frame = tk.Frame(root, bg="#D2B48C")  # Hellbrauner Hintergrund
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Canvas für das Spielfeld
    canvas = Canvas(frame, width=300, height=500, bg="#8B4513", bd=0, highlightthickness=0)
    canvas.pack(pady=20)

    # Farben aus der Variante extrahieren
    farben = [farbe.name for farbe in spielVariante.erlaubteFarben]
    farb_zuordnung = {
        "ROT": "red",
        "GRUEN": "green",
        "BLAU": "blue",
        "GELB": "yellow",
        "ORANGE": "orange",
        "BRAUN": "brown",
        "WEISS": "white",
        "SCHWARZ": "black"
    }

    # Dropdown für Farbauswahl (aktueller Rateversuch)
    farbauswahl_var = StringVar(frame)
    farbauswahl_var.set(farben[0])  # Standardfarbe setzen

    dropdown_frame = tk.Frame(frame, bg="#D2B48C")
    dropdown_frame.pack(pady=5)

    tk.Label(dropdown_frame, text="Aktuelle Farbe:", bg="#D2B48C").pack(side=tk.LEFT)
    dropdown = OptionMenu(dropdown_frame, farbauswahl_var, *farben)
    dropdown.config(bg="#D2B48C")
    dropdown.pack(side=tk.LEFT, padx=5)

    # Spielzeilen (maxVersuche Reihen mit je steckplaetze Löchern)
    steine = {}
    for zeile in range(spielVariante.maxVersuche):
        for spalte in range(spielVariante.steckplaetze):
            # Leere Kreise für die Spielsteine
            id = canvas.create_oval(
                30 + spalte * 40,
                80 + zeile * 40,
                50 + spalte * 40,
                100 + zeile * 40,
                fill="gray50",
                outline="black",
                tags=f"stein_{zeile}_{spalte}"
            )
            steine[(zeile, spalte)] = id
            canvas.tag_bind(id, "<Button-1>",
                          lambda e, z=zeile, s=spalte, f=farbauswahl_var, c=canvas, st=steine:
                              setze_stein(c, z, s, farb_zuordnung[f.get()], st))

        # Kleine Bewertungskreise rechts
        for i in range(2):
            canvas.create_oval(
                190, 85 + zeile * 40 + i * 15,
                200, 95 + zeile * 40 + i * 15,
                fill="gray80",
                outline="black"
            )
            canvas.create_oval(
                210, 85 + zeile * 40 + i * 15,
                220, 95 + zeile * 40 + i * 15,
                fill="gray80",
                outline="black"
            )

    # Farbpalette unten (erlaubte Farben der Variante)
    for i, farbe in enumerate(farben):
        canvas.create_oval(
            30 + i * 30,
            470,
            50 + i * 30,
            490,
            fill=farb_zuordnung[farbe],
            outline="black",
            tags=f"palette_{farbe}"
        )
        canvas.tag_bind(f"palette_{farbe}", "<Button-1>",
                       lambda e, f=farbe: farbauswahl_var.set(f))

    return frame

def setze_stein(canvas, zeile, spalte, farbe, steine):
    canvas.itemconfig(steine[(zeile, spalte)], fill=farbe)
