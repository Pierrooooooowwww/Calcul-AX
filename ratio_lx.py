from utile import arrondi_arithmetique
def calcul_ratio_Lx(lx_exact_vector):
    """
    Calcule le vecteur de (Lx+k) / Lx basé sur le premier Lx exact.

    :param lx_exact_vector: Liste des valeurs Lx exactes.
    :return: Liste des ratios (Lx+k) / Lx.
    """
    if not lx_exact_vector or lx_exact_vector[0] is None:
        raise ValueError("Liste vide ou premier Lx indisponible")

    lx_reference = lx_exact_vector[0]  
    ratio_vector = [lx / lx_reference if lx is not None else None for lx in lx_exact_vector]

    return arrondi_arithmetique(ratio_vector,3)
