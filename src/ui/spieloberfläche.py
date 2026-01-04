import tkinter as tk


def create_spieloberfläche(root):
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    header_frame = tk.Frame(frame)
    header_frame.pack(fill="x", pady=10)

    ueberschrift_Label = tk.Label(
        header_frame,
        text= "Spieloberfläche",
        fg="green",
        font=("Arial", 30, "underline")
    )
    ueberschrift_Label.pack(side="left")

    return frame
