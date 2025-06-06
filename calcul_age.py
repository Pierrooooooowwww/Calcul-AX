import json
from utile import arrondi_arithmetique
from datetime import datetime, timedelta
import calendar

with open("input.json","r", encoding="utf-8") as file:
    payload = json.load(file)

date_contrat = datetime.strptime(payload['date_contrat'],"%d/%m/%Y")
date_rentier = datetime.strptime(payload['date_rentier'],"%d/%m/%Y")
date_conjoint = datetime.strptime(payload['date_conjoint'],"%d/%m/%Y")

def fin_de_mois(date):
    dernier_jour = calendar.monthrange(date.year, date.month)[1]
    return datetime(date.year, date.month, dernier_jour)

def calcul_age_arrondi(date_naissance, date_reference):
    fin_mois_naissance = fin_de_mois(date_naissance)
    partie1 = arrondi_arithmetique(((fin_mois_naissance.day - date_naissance.day + 1) / fin_mois_naissance.day), 3)
    
    mois_precedent_contrat = date_reference.replace(day=1) - timedelta(days=1)
    ecart_annees = (mois_precedent_contrat.year - date_naissance.year) * 12
    ecart_mois = mois_precedent_contrat.month - date_naissance.month

    fin_mois_contrat = fin_de_mois(date_reference)
    partie2 = arrondi_arithmetique(((date_reference.day - 1) / fin_mois_contrat.day), 3)

    age = arrondi_arithmetique(((partie1 + ecart_annees + ecart_mois + partie2) / 12), 3)
    return age

age_rentier_exact = calcul_age_arrondi(date_rentier, date_contrat)
age_conjoint_exact = calcul_age_arrondi(date_conjoint, date_contrat)

age_rentier_arrondi = int(age_rentier_exact)
age_conjoint_arrondi = int(age_conjoint_exact)

