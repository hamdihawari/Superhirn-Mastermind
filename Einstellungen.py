import tkinter as tk
from tkinter import ttk  # Für Combobox (modernere Alternative zu OptionMenu)

root = tk.Tk()
root.title("Einstellungen")
root.geometry("700x500")
root.resizable(width=False, height=False)

# --- Überschrift ---
header_frame = tk.Frame(root)
header_frame.pack(anchor="nw", pady=10)

ueberschrift_Label = tk.Label(
    header_frame,
    text="Einstellungen",
    fg="black",
    font=("Arial", 36, "underline")
)
ueberschrift_Label.pack(side="left")

# --- Haupt-Frame für Farbauswahl ---
upperCenter_frame = tk.Frame(
    root,
    bg="green",
    borderwidth=5,
    padx=10,
    pady=10
)
upperCenter_frame.pack(anchor="nw", fill="x", padx=10, pady=10)

# Überschrift für Farbauswahl
farbauswahl_label = tk.Label(
    upperCenter_frame,
    text="Farbauswahl",
    font=("Arial", 20, "bold"),
)
farbauswahl_label.pack(anchor="w", pady=(0, 10))

# Liste der verfügbaren Farben --> für später sollte hier eher eine getFarben Methode hinzu
farben = ["Rot", "Grün", "Blau", "Gelb"]

# --- 5 Farbauswahl-Blöcke erstellen ---
for i in range(1, 6):  # 1 bis 5
    # Frame für jeden Block (1 Zeile)
    block_frame = tk.Frame(
        upperCenter_frame,
        bg="green")

    block_frame.pack(fill="x", pady=5)

    # 1. Nummer (Label)
    nummer_label = tk.Label(
        block_frame,
        text=f"{i}",
        font=("Arial", 14),
        width=2,
        bg="lightgray"
    )
    nummer_label.pack(side="left", padx=5)

    # 3. Dropdown für Farbauswahl
    farbe_var = tk.StringVar(value=farben[0])  # Standardfarbe: "Rot"


    farbe_option = tk.OptionMenu(
        block_frame,
        farbe_var,
        *farben
    )
    farbe_option.config(font=("Arial", 12), bg="white", width=10)
    farbe_option.pack(side="left", padx=5)


root.mainloop()
