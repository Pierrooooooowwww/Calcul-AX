def arrondi_arithmetique(valeur, nb_decimales) :
    """
    Retourne l'arrondi arithmetique (x.5 devient x+1)
    """

    try : 
        
        facteur = valeur * (10 ** nb_decimales)
        if valeur >= 0:
            if facteur - int(facteur) >= 0.5:
                return (int(facteur) + 1) / (10 ** nb_decimales)
            return int(facteur) / (10 ** nb_decimales)

        if facteur - int(facteur) <= -0.5:
            return (int(facteur) - 1) / (10 ** nb_decimales)
        return int(facteur) / (10 ** nb_decimales)
    
    except :
        
        return valeur