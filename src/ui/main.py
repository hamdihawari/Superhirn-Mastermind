import tkinter as tk
from controller import GameController   # Dateiname anpassen

def main():
    root = tk.Tk()
    root.title("Superhirn")
    root.geometry("800x600")

    GameController(root)

    root.mainloop()

if __name__ == "__main__":
    main()
