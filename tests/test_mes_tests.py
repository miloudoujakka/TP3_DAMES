"""Mes tests (étape 8, bonus) : sauvegarde et reprise d'une partie avec prise."""
from dames import Partie


def test_reprise_apres_une_prise(tmp_path):
    partie = Partie()
    partie.jouer("d4", "c5")
    partie.jouer("e7", "d6")
    partie.jouer("c5", "e7")                       # prise des blancs
    partie.sauvegarder(tmp_path / "partie.json")
    reprise = Partie.charger(tmp_path / "partie.json")
    assert reprise.trait == "noir"
    assert reprise.plateau.compter("noir") == 19
    assert reprise.plateau.vers_dict() == partie.plateau.vers_dict()
    # le bon joueur doit encore pouvoir prendre : f8 saute e7 pour aller en d6
    reprise.jouer("f8", "d6")
    assert reprise.trait == "blanc"
