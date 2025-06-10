import pandas as pd
import math
from datetime import datetime, timedelta
import calendar
from dernier_jour_fractionnement import fin_periode

def fin_de_mois(date):
    """Retourne la date de fin de mois pour une date donnée."""
    dernier_jour = calendar.monthrange(date.year, date.month)[1]
    return datetime(date.year, date.month, dernier_jour)


def generer_fins_de_mois(date_debut, age_limite= 120):
    """
    Génère toutes les dates de fin de mois à partir de la date de début jusqu'à 120 ans après.
    
    :param date_debut: Date de début du versement des retraites
    :param age_limite: Nombre d'années à couvrir (par défaut 120)
    :return: Liste des dates de fin de mois
    """
    dates = []
    date_courante = date_debut
    date_limite = date_debut.replace(year=date_debut.year + age_limite)

    while date_courante <= date_limite:
        dates.append(fin_de_mois(date_courante))
    
        if date_courante.month == 12:
            date_courante = date_courante.replace(year=date_courante.year + 1, month=1)
        else:
            date_courante = date_courante.replace(month=date_courante.month + 1)

    return dates

# def generer_dates_jusqua_limite(date_debut, age_rentier, age_conjoint, frequence):
#     """
#     Génère les dates de fin de période jusqu'à ce que les deux âges soient > 120 ans et retourne aussi les tableaux des ages exact de Rentier et Conjoint
    
#     :param date_debut: Date de départ
#     :param age_rentier: Age initial du rentier
#     :param age_conjoint: Age initial du conjoint
#     :param frequence: Fréquence du versement (mensuel, trimestriel, etc.)
#     :return: Liste des dates de fin de période
#     """
#     frequence = frequence.lower()
#     delta_mois = {
#         'mensuel': 1, #12
#         'trimestriel': 3, #4
#         'semestriel': 6, #2
#         'annuel': 12 #1
#     }.get(frequence)

#     dates = []
#     date_courante = date_debut

#     while age_rentier < 121 or age_conjoint < 121:
#         dates.append(fin_periode(date_courante, frequence))
#         age_rentier += delta_mois / 12
#         age_conjoint += delta_mois / 12

        
#         mois_suivant = date_courante.month + delta_mois
#         annee_suivante = date_courante.year + (mois_suivant - 1) // 12
#         mois_suivant = (mois_suivant - 1) % 12 + 1
#         date_courante = datetime(annee_suivante, mois_suivant, 1)

#     return dates 

def generer_dates_jusqua_limite(date_debut: datetime, age_rentier: float, age_conjoint: float, frequence: str = "mensuel") -> tuple[list[datetime], list[float], list[float]]:
    """
    Génère les dates de fin de période jusqu'à ce que les deux âges soient > 120 ans,
    en retournant aussi les listes d'âges correspondantes pour rentier et conjoint.

    :param date_debut: Date de départ
    :param age_rentier: Age initial du rentier
    :param age_conjoint: Age initial du conjoint
    :param frequence: Fréquence du versement (mensuel, trimestriel, etc.)
    :return: Tuple (dates, ages_rentier, ages_conjoint)
    """
    frequence = frequence.lower()
    delta_mois = {
        'mensuel': 1,
        'trimestriel': 3,
        'semestriel': 6,
        'annuel': 12
    }.get(frequence)

    if delta_mois is None:
        raise ValueError("Fréquence non supportée. Utilisez : mensuel, trimestriel, semestriel, annuel")
    
    dates = []
    ages_rentier = []
    ages_conjoint = []

    date_courante = date_debut

    while age_rentier < 120 or age_conjoint < 120:
        dates.append(fin_periode(date_courante, frequence))
        ages_rentier.append(round(age_rentier, 6))
        ages_conjoint.append(round(age_conjoint, 6))

        age_rentier += delta_mois / 12
        age_conjoint += delta_mois / 12

        mois_suivant = date_courante.month + delta_mois
        annee_suivante = date_courante.year + (mois_suivant - 1) // 12
        mois_suivant = (mois_suivant - 1) % 12 + 1
        date_courante = datetime(annee_suivante, mois_suivant, 1)

    return dates, ages_rentier, ages_conjoint