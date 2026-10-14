# Cargamos librerías a utilizar
import pandas as pd
import numpy as np
from scipy import stats

# Librerías para graficar
import matplotlib.pyplot as plt
import seaborn as sns

# Solicitar los permisos para trabajar con el excel

ruta = 'Social_media_impact_on_life.xlsx'
df = pd.read_excel(ruta)
df.head()