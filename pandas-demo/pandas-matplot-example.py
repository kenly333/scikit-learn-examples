import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    df_train = pd.read_csv('../Datasets/Breast-Cancer/breast-cancer-train.csv')
    df_test = pd.read_csv('../Datasets/Breast-Cancer/breast-cancer-test.csv')

    df_test_negative = df_test.loc[df_test['Type'] == 0][['Clump Thickness', 'Cell Size']]
    df_test_positive = df_test.loc[df_test['Type'] == 1][['Clump Thickness', 'Cell Size']]

    # ------------------------------------------------------------------------------------------

    plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='o', s=200, c='red')
    plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=150, c='black')

    plt.xlabel('Clump Thickness')
    plt.ylabel('Cell Size')

    plt.show()

    # ------------------------------------------------------------------------------------------

    intercept = np.random.random([1])
    coef = np.random.random([2])

    lx = np.arange(0, 12)
    ly = (-intercept - lx * coef[0]) / coef[1]

    plt.plot(lx, ly, c='yellow')

    plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='o', s=200, c='red')
    plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=150, c='black')
    plt.xlabel('Clump Thickness')
    plt.ylabel('Cell Size')
    plt.show()

    # ------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
