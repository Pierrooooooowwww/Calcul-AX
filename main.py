import json
from calcul_age import calcul_age_exact
import pandas as pd
from datetime import datetime
from dernier_jour_fractionnement import fin_periode
from recherche_table_mortalité import trouver_Lx
import math
from affichage_des_fins_de_mois import generer_dates_jusqua_limite
with open("data/input.json","r", encoding="utf-8") as file:
    payload = json.load(file)

recherche_table_mortalité = pd.read_csv("Table.csv",sep=";")

date_contrat = datetime.strptime(payload['date_contrat'],"%d/%m/%Y")
date_rentier = datetime.strptime(payload['date_rentier'],"%d/%m/%Y")
date_conjoint = datetime.strptime(payload['date_conjoint'],"%d/%m/%Y")

age_rentier_exact = calcul_age_exact(date_rentier, date_contrat)
age_conjoint_exact = calcul_age_exact(date_conjoint, date_contrat)

affichage_tout_les_mois = generer_dates_jusqua_limite(date_contrat,age_rentier_exact,age_conjoint_exact,payload['fractionnement']) 

# LX = trouver_Lx(age_rentier_exact,int(date_rentier.year),recherche_table_mortalité)
# LY = trouver_Lx(age_conjoint_exact, int(date_conjoint.year),recherche_table_mortalité)

# LX_plus_1 = trouver_Lx(age_rentier_exact+1,int(date_rentier.year),recherche_table_mortalité)
# LY_plus_1 = trouver_Lx(age_conjoint_exact+1, int(date_conjoint.year),recherche_table_mortalité)



