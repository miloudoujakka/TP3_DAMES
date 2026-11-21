"""Jouer aux dames à deux dans le terminal : chaque joueur tape son coup, comme c3 d4."""
from dames import Partie
from exceptions import ErreurDames

FICHIER = "partie.json"


def lire_coup(texte: str) -> tuple[str, str]:
    """« c3 d4 », « c3-d4 » ou « d4xf6 » donnent ("c3", "d4"). Sinon ValueError."""
    morceaux = texte.replace("-", " ").replace("x", " ").split()
    if len(morceaux) != 2:
        raise ValueError("tapez deux cases, par exemple c3 d4")
    return morceaux[0], morceaux[1]


def main() -> int:
    partie = Partie()
    print(partie.plateau)
    while partie.gagnant is None:
        saisie = input(f"{partie.trait} > ").strip()
        if saisie == "quitter":
            print("Partie abandonnée.")
            return 0
        if saisie == "sauver":
            partie.sauvegarder(FICHIER)
            print(f"Partie sauvegardée dans {FICHIER}.")
            continue
        if saisie == "reprendre":
            try:
                partie = Partie.charger(FICHIER)
            except (OSError, ValueError, KeyError) as erreur:
                print(f"Refusé : impossible de reprendre la partie ({erreur})")
                continue
            print(partie.plateau)
            continue
        try:
            depart, arrivee = lire_coup(saisie)
            coup = partie.jouer(depart, arrivee)
        except (ErreurDames, ValueError) as erreur:
            print(f"Refusé : {erreur}")
            continue
        print(coup)
        print(partie.plateau)
    print(f"Les {partie.gagnant}s gagnent !")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
