import pandas as pd
from datetime import datetime
import math

def trouver_Lx(age, annee_naissance, table):
    age_plancher = math.floor(age)
    ligne = table[table['Age'] == age_plancher]
    lx = ligne[str(annee_naissance)].values[0]
    return int(lx)

