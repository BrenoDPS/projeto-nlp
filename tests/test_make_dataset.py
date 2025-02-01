from data_processing.mesclar_datasets import null_values
import pytest
import pandas as pd
import numpy as np

@pytest.fixture
def data_values():

    dict_data = {"Column 1": [0, 1, 0, 2, None], 
                 "Column 2": [None, None, None, False, False]}
    
    yield pd.DataFrame(dict_data)


def test_null_values(data_values):

    out = null_values(data_values)
    exp = pd.Series(data = [20.00, 60.00], index = ["Column 1", "Column 2"])

    assert np.all(out.index == exp.index)

    assert np.all(out.values == exp.values)