import math
from utile import arrondi_arithmetique

def calcul_Lx_exact_vector(ages_rentier, lx_values, lx_plus_1_values):
    """
    Calcule le vecteur complet des Lx exacts pour tous les âges du rentier.

    :param ages_rentier: Liste des âges du rentier.
    :param lx_values: Liste des valeurs Lx.
    :param lx_plus_1_values: Liste des valeurs Lx+1.
    :param nb_decimales: Nombre de décimales pour l'arrondi.
    :return: Liste des valeurs Lx exactes arrondies.
    """
    lx_exact_vector = []
    
    for age_decimal, lx, lx_plus_1 in zip(ages_rentier, lx_values, lx_plus_1_values):
        if lx is not None and lx_plus_1 is not None:
            lx_exact = (1 - age_decimal % 1) * lx + (age_decimal % 1) * lx_plus_1
            lx_exact_vector.append(arrondi_arithmetique(lx_exact, 3))
        else:
            lx_exact_vector.append(None) 

    return lx_exact_vector

