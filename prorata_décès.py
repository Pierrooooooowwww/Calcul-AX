from utile import arrondi_arithmetique

def calcul_vecteur_prorata_deces(lx_exact_vector, ly_exact_vector, taux_reversion):
    """
    Calcule le vecteur du prorata décès via la formule :
    ((Lx1 - Lx2) / Lx_base) * (1 - taux_reversion * Ly2 / Ly_base) + 
    ((Ly1 - Ly2) / Ly_base) * (1 - Lx1 / Lx_base) * taux_reversion.

    :param lx_exact_vector: Liste des Lx exacts.
    :param ly_exact_vector: Liste des Ly exacts.
    :param taux_reversion: Taux de réversion 
    :return: Liste des proratas décès calculés.
    """
    if not lx_exact_vector or lx_exact_vector[0] is None:
        raise ValueError("Liste vide ou premier Lx indisponible")
    
    if not ly_exact_vector or ly_exact_vector[0] is None:
        raise ValueError("Liste vide ou premier Ly indisponible")

    lx_base = lx_exact_vector[0]  
    ly_base = ly_exact_vector[0]  

    prorata_vector = []
    
    for i in range(len(lx_exact_vector) - 1): 
        lx1, lx2 = lx_exact_vector[i], lx_exact_vector[i + 1]
        ly1, ly2 = ly_exact_vector[i], ly_exact_vector[i + 1]

        if None not in (lx1, lx2, ly1, ly2):
            prorata = ((lx1 - lx2) / lx_base) * (1 - taux_reversion * ly2 / ly_base) + \
                      ((ly1 - ly2) / ly_base) * (1 - lx1 / lx_base) * taux_reversion
            prorata_vector.append(prorata)  
        else:
            prorata_vector.append(None) 
    
    return prorata_vector
