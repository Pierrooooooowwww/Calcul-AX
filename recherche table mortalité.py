import json
from calcul_age import calcul_age_exact
import pandas as pd
from datetime import datetime
import math
from utile import arrondi_arithmetique

with open("data/input.json","r", encoding="utf-8") as file:
    payload = json.load(file)

recherche_table_mortalité = pd.read_csv("Table.csv",sep=";")

date_contrat = datetime.strptime(payload['date_contrat'],"%d/%m/%Y")
date_rentier = datetime.strptime(payload['date_rentier'],"%d/%m/%Y")
date_conjoint = datetime.strptime(payload['date_conjoint'],"%d/%m/%Y")

age_rentier_exact = calcul_age_exact(date_rentier, date_contrat)
age_conjoint_exact = calcul_age_exact(date_conjoint, date_contrat)

def trouver_Lx(age, annee_naissance, table):
    age_plancher = math.floor(age)
    ligne = table[table['Age'] == age_plancher]
    lx = ligne[str(annee_naissance)].values[0]
    return int(lx)

LX = trouver_Lx(age_rentier_exact,int(date_rentier.year),recherche_table_mortalité)
LY = trouver_Lx(age_conjoint_exact, int(date_conjoint.year),recherche_table_mortalité)

LX_plus_1 = trouver_Lx(age_rentier_exact+1,int(date_rentier.year),recherche_table_mortalité)
LY_plus_1 = trouver_Lx(age_conjoint_exact+1, int(date_conjoint.year),recherche_table_mortalité)

