from anwendung.modus import Modus


class Sichtbarkeiten:
    @staticmethod
    def get_sichtbarkeit(modus: Modus) -> dict:
        """Gibt ein Dictionary mit Sichtbarkeits-Einstellungen für den gegebenen Modus zurück"""
        if modus == Modus.C_M_ONLINE or modus == Modus.C_C_ONLINE:
            return {
                "show_farbe": False,
                "show_algorithmus": False,
                "show_zeit": False,
                "show_code_auswahl": False,
                "show_code_auswahl_spiel_ui": True,
                "show_knuth_vs_step": False  # Neue Eigenschaft
            }
        elif modus == Modus.C_M:  # Expliziter Vergleich statt `in`
            return {
                "show_farbe": False,
                "show_algorithmus": False,
                "show_zeit": False,
                "show_code_auswahl": False,
                "show_code_auswahl_spiel_ui": True,
                "show_knuth_vs_step": False  # Neue Eigenschaft
            }
        elif modus == Modus.C_C:
            return {
                "show_farbe": True,
                "show_algorithmus": True,
                "show_zeit": True,
                "show_code_auswahl": False,
                "show_code_auswahl_spiel_ui": False,
                "show_knuth_vs_step": False  # Neue Eigenschaft
            }
        else:  # Modus.M_C
            return {
                "show_farbe": True,
                "show_algorithmus": True,
                "show_zeit": True,
                "show_code_auswahl": True,
                "show_code_auswahl_spiel_ui": False,
                "show_knuth_vs_step": True  # Neue Eigenschaft
            }
