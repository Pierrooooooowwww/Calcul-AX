# import pandas as pd
# import math
# from datetime import datetime, timedelta
# import calendar

# def fin_de_mois(date):
#     """Retourne la date de fin de mois pour une date donnée."""
#     dernier_jour = calendar.monthrange(date.year, date.month)[1]
#     return datetime(date.year, date.month, dernier_jour)

# def generer_fins_de_mois(date_debut, age_limite= 120):
#     """
#     Génère toutes les dates de fin de mois à partir de la date de début jusqu'à 120 ans après.
    
#     :param date_debut: Date de début du versement des retraites
#     :param age_limite: Nombre d'années à couvrir (par défaut 120)
#     :return: Liste des dates de fin de mois
#     """
#     dates = []
#     date_courante = date_debut
#     date_limite = date_debut.replace(year=date_debut.year + age_limite)

#     while date_courante <= date_limite:
#         dates.append(fin_de_mois(date_courante))
    
#         if date_courante.month == 12:
#             date_courante = date_courante.replace(year=date_courante.year + 1, month=1)
#         else:
#             date_courante = date_courante.replace(month=date_courante.month + 1)

#     return dates

