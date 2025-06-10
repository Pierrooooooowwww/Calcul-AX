import json
from calcul_age import calcul_age_exact
import pandas as pd
from datetime import datetime
from dernier_jour_fractionnement import fin_periode
from recherche_table_mortalité import calculer_lx_vector
import math
from affichage_des_fins_de_mois import generer_dates_jusqua_limite
from calcul_lx_exact import calcul_Lx_exact_vector
from ratio_lx import calcul_ratio_Lx
from lx_ly_ratio import calcul_ratio_Lx_Ly
from utile import arrondi_arithmetique
from calcul_actualisation import calcul_vecteur_actualisation



with open("data/input.json","r", encoding="utf-8") as file:
    payload = json.load(file)

table_mortalité_TGM05 = pd.read_csv("Table.csv",sep=";") #Table de Mortalité TGM05

date_contrat = datetime.strptime(payload['date_contrat'],"%d/%m/%Y")
date_rentier = datetime.strptime(payload['date_rentier'],"%d/%m/%Y")
date_conjoint = datetime.strptime(payload['date_conjoint'],"%d/%m/%Y")

age_rentier_exact = calcul_age_exact(date_rentier, date_contrat)
age_conjoint_exact = calcul_age_exact(date_conjoint, date_contrat)

affichage_tout_les_mois = generer_dates_jusqua_limite(date_contrat,age_rentier_exact,age_conjoint_exact,payload['fractionnement']) 

lX_vector = calculer_lx_vector(affichage_tout_les_mois[1],date_rentier.year,table_mortalité_TGM05 )
lY_vector = calculer_lx_vector(affichage_tout_les_mois[2],date_conjoint.year,table_mortalité_TGM05 )

lX_vector_exact = calcul_Lx_exact_vector(affichage_tout_les_mois[1],lX_vector[0],lX_vector[1])
lY_vector_exact = calcul_Lx_exact_vector(affichage_tout_les_mois[2],lY_vector[0],lY_vector[1])

lX_vector_ratio = calcul_ratio_Lx(lX_vector_exact)
lY_vector_ratio = calcul_ratio_Lx(lY_vector_exact)

lX_lY_vector_ratio = calcul_ratio_Lx_Ly(lX_vector_exact, lY_vector_exact) # Calcul du (1-px)*py sur le Excel

