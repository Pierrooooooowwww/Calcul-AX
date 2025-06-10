import pandas as pd
from datetime import datetime
import math


def calculer_lx_vector(ages_rentier, annee_naissance, table):
    """
    Retourne un vecteur contenant tous les Lx pour les âges donnés du rentier.

    :param ages_rentier: Liste des âges du rentier.
    :param annee_naissance: Année de naissance du rentier.
    :param table: Table de mortalité sous forme de DataFrame.
    :return: Liste des valeurs Lx correspondant aux âges du rentier.
    """
    lx_vector = []
    lx_plus_1_vector = []
    
    for age in ages_rentier:  
        age_plancher = math.floor(age)  
        ligne = table[table['Age'] == age_plancher]  
        ligne_plus_1 = table[table['Age'] == age_plancher + 1]  
        
        if not ligne.empty:
            lx_vector.append(int(ligne[str(annee_naissance)].values[0])) 
        if not ligne_plus_1.empty:
            lx_plus_1_vector.append(int(ligne_plus_1[str(annee_naissance)].values[0])) 

    return lx_vector,lx_plus_1_vector
