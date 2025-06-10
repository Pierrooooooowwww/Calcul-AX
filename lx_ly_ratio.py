def calcul_ratio_Lx_Ly(lx_exact_vector, ly_exact_vector):
    """
    Calcule le vecteur de (((1 - Lx_exact / Lx_reference)) * (Ly_exact / Ly_reference)).

    :param lx_exact_vector: Liste des valeurs Lx exactes.
    :param ly_exact_vector: Liste des valeurs Ly exactes.
    :return: Liste des ratios calculés.
    """
    if not lx_exact_vector or lx_exact_vector[0] is None:
        raise ValueError("Liste vide ou premier Lx indisponible")
    
    if not ly_exact_vector or ly_exact_vector[0] is None:
        raise ValueError("Liste vide ou premier Ly indisponible")

    lx_reference = lx_exact_vector[0]  
    ly_reference = ly_exact_vector[0]  
    
    ratio_vector = [((1 - lx / lx_reference) * (ly / ly_reference)) if lx is not None and ly is not None else None for lx, ly in zip(lx_exact_vector, ly_exact_vector)]

    return ratio_vector
