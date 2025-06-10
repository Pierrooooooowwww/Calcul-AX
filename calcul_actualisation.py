def calcul_vecteur_actualisation(ages_exact_vector, taux_effectif, age_reference):
    """
    Calcule le vecteur d'actualisation via la formule : 1 / (1 + taux_effectif)^(age_exact - age_reference).

    :param ages_exact_vector: Liste des âges exacts.
    :param taux_effectif: Taux effectif (B7 en Excel).
    :param age_reference: Âge exact stocké (B5 en Excel).
    :return: Liste des coefficients d'actualisation.
    """
    actualisation_vector = [1 / (1 + taux_effectif)**(age - age_reference) if age is not None else None for age in ages_exact_vector]
    
    return actualisation_vector
