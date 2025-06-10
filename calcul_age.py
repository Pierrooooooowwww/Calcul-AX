import json
from utile import arrondi_arithmetique
from datetime import datetime, timedelta
import calendar
import os

def fin_de_mois(date):
    dernier_jour = calendar.monthrange(date.year, date.month)[1]
    return datetime(date.year, date.month, dernier_jour)

def calcul_age_exact(date_naissance, date_reference):
    fin_mois_naissance = fin_de_mois(date_naissance)
    partie1 = arrondi_arithmetique(((fin_mois_naissance.day - date_naissance.day + 1) / fin_mois_naissance.day), 3)
    
    mois_precedent_contrat = date_reference.replace(day=1) - timedelta(days=1)
    ecart_annees = (mois_precedent_contrat.year - date_naissance.year) * 12
    ecart_mois = mois_precedent_contrat.month - date_naissance.month

    fin_mois_contrat = fin_de_mois(date_reference)
    partie2 = arrondi_arithmetique(((date_reference.day - 1) / fin_mois_contrat.day), 3)

    age = arrondi_arithmetique(((partie1 + ecart_annees + ecart_mois + partie2) / 12), 3)
    return age

