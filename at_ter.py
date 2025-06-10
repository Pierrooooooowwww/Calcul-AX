def calcul_vecteur_at_TER(periodes_vector, fractionnement, annuites_garanties, annuites_garanties_vector, majoration_apres, taux_majoration, at_TER_vector):
    """
    Calcule le vecteur 'AT TER' selon la même logique que 'AT bis'.

    :param periodes_vector: Liste des périodes (D11).
    :param fractionnement: Fractionnement souhaité (E1).
    :param annuites_garanties: Annuités garanties (B10).
    :param annuites_garanties_vector: Liste des annuités garanties (V11).
    :param majoration_apres: Seuil de majoration après (B15).
    :param taux_majoration: Pourcentage de majoration (B16).
    :param at_TER_vector: Liste des valeurs AT TER (Y11).
    :return: Liste des valeurs du vecteur 'AT TER'.
    """
    at_TER_result = []
    
    for periode, v_annuite, y_at_TER in zip(periodes_vector, annuites_garanties_vector, at_TER_vector):
        valeur_test = periode / fractionnement  # D11 / E1
        
        if valeur_test < annuites_garanties + (1 / fractionnement):
            at_TER_result.append(v_annuite)  # V11
        elif valeur_test < majoration_apres + (1 / fractionnement):
            at_TER_result.append(y_at_TER)  # Y11
        else:
            at_TER_result.append(round(y_at_TER * (1 + taux_majoration), 4))  # Y11 * (1 + B16), arrondi à 4 décimales

    return at_TER_result
