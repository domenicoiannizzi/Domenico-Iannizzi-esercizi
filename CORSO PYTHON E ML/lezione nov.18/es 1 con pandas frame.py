#creare df con 10 righe e 3 colonne di numeri randomici

import numpy as np
import pandas as pd

df=pd.DataFrame({
    'c1': np.random.randint(1,25,10),
    'c2': np.random.randint(1,25,10),
    'c3': np.random.randint(1,25,10),
})
df
