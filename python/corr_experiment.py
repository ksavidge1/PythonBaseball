import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from read_rawCSV import read_raw
from scipy.stats import pearsonr

source_path = Path('C:/Testing/Pybaseball/RawCSV')
csv_filename = 'batting/18.csv'

ind = 'BB%'
dep = 'wRC+'


def corr_2_stats(csv_data, ind_var, dep_var):

    ind_var_data = csv_data[ind_var].values
    dep_var_data = csv_data[dep_var].values
    num_vals = len(ind_var_data)

    corr_val, _ = pearsonr(ind_var_data, dep_var_data)
    print('# of value-pairs considered: %i \n' % num_vals)
    print('Correlation: %.3f \n' % corr_val)

    plt.scatter(ind_var_data, dep_var_data)
    plt.xlabel(ind_var)
    plt.ylabel(dep_var)
    plt.title('N = ' + str(num_vals))
    plt.show()

    print('Done')

    return


def main():

    # Load a specified csv file as Dataframe
    csv_data = read_raw(source_path, csv_filename)

    # Simple processing of 2 incoming stat columns
    corr_2_stats(csv_data, ind, dep)

    return


if __name__ == '__main__':
    main()
