import tkinter as tk
from typing import List

from anwendung.spielengine import VergleichsEngine
from anwendung.spielstart import Spielstarter
from anwendung.modus import Modus

from src.anwendung.spielparameter import Spielparameter
from src.spiel.farbe import Farbe
from spiel.variante import Variante
from spiel.spielCodes import Code
from ui.sprache import Sprache


class GameController:

    def __init__(self, root: tk.Tk):
        self.root = root

        # Frames
        self.uebersicht_frame = None
        self.spieleinstellungen_frame = None
        self.spieloberflaeche_frame = None

        # Spielzustand
        self.spielVariante = Variante.SUPER
        self.spielModus = Modus.M_C
        self.spielAlgorithmus = "knuth"
        self.spielSprache = Sprache.DEUTSCH

        # Engine & Timing
        self.spiel_engine = None
        self.delay = 1  # Sekunden

        self.show_uebersicht()

    # --------------------------------------------------
    # UI: Übersicht
    # --------------------------------------------------
    def show_uebersicht(self):
        self._clear_frames()

        from Uebersichtsbildschirm import create_uebersicht_frame
        self.uebersicht_frame = create_uebersicht_frame(
            self.root,
            self.show_spieleinstellungen,
            self.set_variante,
            self.set_modus,
            self.set_sprache,
            self.spielSprache
        )
        self.uebersicht_frame.pack(fill="both", expand=True)

    # --------------------------------------------------
    # UI: Spieleinstellungen
    # --------------------------------------------------
    def show_spieleinstellungen(self):
        self._clear_frames()

        from Spieleinstellungen import create_spieleinstellungen_superhirn_frame
        self.spieleinstellungen_frame = create_spieleinstellungen_superhirn_frame(
            self.root,
            self.show_uebersicht,
            self.on_code_spiel_start,
            self.set_algorithm,
            self.spielVariante.steckplaetze,
            self.spielVariante,
            self.spielModus,
            self.spielSprache
        )
        self.spieleinstellungen_frame.pack(fill="both", expand=True)

    # --------------------------------------------------
    # SETTER
    # --------------------------------------------------
    def set_variante(self, variante: Variante):
        self.spielVariante = variante

    def set_modus(self, modus: Modus):
        self.spielModus = modus

    def set_sprache(self, sprache: Sprache):
        self.spielSprache = sprache

    def set_algorithm(self, algorithmus: str):
        self.spielAlgorithmus = algorithmus

    # --------------------------------------------------
    # SPIELSTART
    # --------------------------------------------------
    def on_code_spiel_start(self, code: Code, zeit: int):

        self.delay = zeit

        algorithmus = (
            self.spielAlgorithmus
            if self.spielModus.rater == "computer"
            else None
        )

        spielparameter = Spielparameter(
            variante=self.spielVariante,
            modus=self.spielModus,
            algorithmus=algorithmus,
            delay=zeit,
            code=code
        )

        starter = Spielstarter()
        self._clear_frames()

        # Vergleichsmodus
        if algorithmus == "beide_algorithmen":
            p1 = Spielparameter(
                self.spielVariante, self.spielModus, "knuth", zeit, code
            )
            p2 = Spielparameter(
                self.spielVariante, self.spielModus, "step_by_step", zeit, code
            )

            e1 = starter.starteSpiel(p1)
            e2 = starter.starteSpiel(p2)

            self.spiel_engine = VergleichsEngine(e1, e2)
            self.setup_ui_vergleich(spielparameter)


        # Singlemodus
        else:
            self.spiel_engine = starter.starteSpiel(spielparameter)
            self.setup_ui_single(spielparameter)



    # --------------------------------------------------
    # UI SETUP
    # --------------------------------------------------
    def setup_ui_single(self, spielparameter):
        from ui.spieloberfläche import create_spieloberfläche

        (
            self.spieloberflaeche_frame,
            self.zeige_feedback,
            self.zeige_code,
            self.zeige_fehler
        ) = create_spieloberfläche(
            self.root,
            spielparameter,
            self.on_rateversuch_mensch_rater,
            self.spielModus
        )

        self.spieloberflaeche_frame.pack(fill="both", expand=True)


        if self.spielModus.rater == "computer":
            self.root.after(100, self.auto_raten_single)

    def setup_ui_vergleich(self, spielparameter):
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)
        self.spieloberflaeche_frame = container

        left = tk.Frame(container)
        right = tk.Frame(container)
        left.pack(side="left", fill="both", expand=True)
        right.pack(side="right", fill="both", expand=True)

        from ui.spieloberfläche import create_spieloberfläche

        (_, self.zeige_feedback_A, self.zeige_code_A, _) = create_spieloberfläche(
            left, spielparameter, None, self.spielModus
        )

        (_, self.zeige_feedback_B, self.zeige_code_B, _) = create_spieloberfläche(
            right, spielparameter, None, self.spielModus
        )

        self.root.after(100, self.auto_raten_vergleich)

    # --------------------------------------------------
    # CALLBACKS
    # --------------------------------------------------
    def on_rateversuch_mensch_rater(self, versuch: List[str], zeile: int):
        farb_versuch = Code([Farbe[farbe] for farbe in versuch])
        farb_namen = [f.name for f in farb_versuch.farben]
        print(f"Farben des Rateversuchs: {farb_namen}")

        feedback = self.spiel_engine.fuehreZugAus(farb_versuch)
        print(f"Feedback: {feedback.schwarz} schwarz, {feedback.weiss} weiß")
        self.zeige_feedback(zeile, feedback)

    def auto_raten_single(self):
        if not self.spiel_engine.istFertig():
            self.spiel_engine.fuehreZugAus(None)
            letzte = self.spiel_engine.letzteRunde()

            z = letzte.rundenNr - 1
            self.zeige_feedback(z, letzte.feedback)
            self.zeige_code(z, letzte.code)

            self.root.after(self.delay * 1000, self.auto_raten_single)

    def auto_raten_vergleich(self):
        if not self.spiel_engine.istFertig():
            self.spiel_engine.fuehreZugAus(None)
            r = self.spiel_engine.letzteRunde()

            z = r["A"].rundenNr - 1

            self.zeige_feedback_A(z, r["A"].feedback)
            self.zeige_code_A(z, r["A"].code)

            self.zeige_feedback_B(z, r["B"].feedback)
            self.zeige_code_B(z, r["B"].code)

            self.root.after(self.delay * 1000, self.auto_raten_vergleich)

    # --------------------------------------------------
    # HELPER
    # --------------------------------------------------
    def _clear_frames(self):
        for frame in (
            self.uebersicht_frame,
            self.spieleinstellungen_frame,
            self.spieloberflaeche_frame
        ):
            if frame:
                frame.destroy()
