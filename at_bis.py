def calcul_vecteur_at_bis(periodes_vector, fractionnement, annuites_garanties_stockees, annuites_garanties, majoration_apres, taux_majoration, at_TER_vector):
    """
    Calcule le vecteur 'at bis' en suivant la formule Excel.

    :param periodes_vector: Liste des périodes (D11).
    :param fractionnement: Fractionnement souhaité (E1).
    :param annuites_garanties_stockees: Valeur stockée des annuités garanties (B10).
    :param annuites_garanties: Liste des annuités garanties (V11).
    :param majoration_apres: Seuil de majoration après (B15).
    :param taux_majoration: Pourcentage de majoration (B16).
    :param at_TER_vector: Liste des valeurs AT TER (Y11).
    :return: Liste des valeurs du vecteur 'at bis'.
    """
    at_bis_vector = []
    
    for periode, v_annuite, y_at_TER in zip(periodes_vector, annuites_garanties, at_TER_vector):
        valeur_test = periode / fractionnement  # D11 / E1
        
        if valeur_test < annuites_garanties_stockees + (1 / fractionnement):
            at_bis_vector.append(v_annuite)  # V11
        elif valeur_test < majoration_apres + (1 / fractionnement):
            at_bis_vector.append(y_at_TER)  # Y11
        else:
            at_bis_vector.append(round(y_at_TER * (1 + taux_majoration), 4))  # Y11 * (1 + B16), arrondi à 4 décimales

    return at_bis_vector
