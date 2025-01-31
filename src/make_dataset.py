import pandas as pd

def null_values(data: pd.DataFrame):

    # função que calcula a pct de valores nulos em cada coluna

    pct = (data.isnull().sum() / data.shape[0] ) * 100

    return pct.round(2)