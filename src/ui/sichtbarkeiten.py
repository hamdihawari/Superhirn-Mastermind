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
                "show_code_auswahl": False
            }
        elif modus == Modus.C_M or modus == Modus.C_C:  # Expliziter Vergleich statt `in`
            return {
                "show_farbe": False,
                "show_algorithmus": False,
                "show_zeit": True,
                "show_code_auswahl": False
            }
        else:  # Modus.M_C
            return {
                "show_farbe": True,
                "show_algorithmus": True,
                "show_zeit": True,
                "show_code_auswahl": True
            }
