import pandas as pd

ri = pd.read_csv('../resources/ArriveDistribution/2.csv')
ri = ri['Ri'].str.replace(',', '.')
ri = pd.to_numeric(ri)
ri = ri.values.tolist()


def get_ri():
    return ri
