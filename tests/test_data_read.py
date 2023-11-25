import sys
import os
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.data_read

def test_read_data():

    all_dat = src.data_read.get_all_data()

    # check is a dataframe
    assert isinstance(all_dat, pd.DataFrame)

    # check column names
    assert list(all_dat.columns) == ['gspc',
                                     'gspc_next_year_pct_chg',
                                     'gspc_prev_year_pct_chg',
                                     'inflation_rate_pct',
                                     'inflation_rate_pct_chg',
                                     'interest_rate_pct',
                                     'interest_rate_pct_chg',
                                     'target']

    # check numeric columns
    assert list(all_dat.select_dtypes(include='float64').columns) == ['gspc',
                                                                      'gspc_next_year_pct_chg',
                                                                      'gspc_prev_year_pct_chg',
                                                                      'inflation_rate_pct',
                                                                      'inflation_rate_pct_chg',
                                                                      'interest_rate_pct',
                                                                      'interest_rate_pct_chg']
    # check boolean columns
    assert list(all_dat.select_dtypes(include='bool').columns) == ['target']

    # check index start and end
    assert all_dat.index[0] == pd.DatetimeIndex(['1955-07-31'])
    assert all_dat.index[-1] == pd.DatetimeIndex(['2022-10-31'])

    # check index is increasing
    assert all_dat.index.is_monotonic_increasing

    # check index is unique
    assert all_dat.index.is_unique

    # check no na
    assert not all_dat.isna().any(axis=None)

    return