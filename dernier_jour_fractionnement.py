import pandas as pd
import math
from datetime import datetime, timedelta
import calendar


def fin_de_mois(date):
    """Retourne la date de fin de mois pour une date donnée."""
    dernier_jour = calendar.monthrange(date.year, date.month)[1]
    return datetime(date.year, date.month, dernier_jour)

def fin_periode(date, frequence):
    """
    Calcule la fin de période selon la fréquence : mensuel, trimestriel, semestriel, annuel

    :param date: date de départ
    :param frequence: 'mensuel', 'trimestriel', 'semestriel', 'annuel'
    :return: dernier jour de la période
    """
    frequence = frequence.lower()
    delta = {
        'mensuel': 1,
        'trimestriel': 3,
        'semestriel': 6,
        'annuel': 12
    }.get(frequence)

    if delta is None:
        raise ValueError("Fréquence non supportée. Utilisez : mensuel, trimestriel, semestriel, annuel")

    mois_fin = date.month + delta - 1
    annee_fin = date.year + (mois_fin - 1) // 12
    mois_fin = (mois_fin - 1) % 12 + 1

    return fin_de_mois(datetime(annee_fin, mois_fin, 1))
