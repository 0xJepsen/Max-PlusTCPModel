from Topologies import linear, simple_branch
from Validation import validate_Y, validate_Z
import pandas as pd
from pprint import pprint


def model_config(conf, df0):
    pass


def main():
    df0, ps0, conf0 = linear()
    (df1, df2), (ps1, ps2), (conf1, conf2) = simple_branch()

    print(df0)
    dict = df0.to_dict()
    # pprint(dict['Size'])

    model_config(conf0, df0)

    # validate_Z(df0, ps0, conf0, )
    # validate_Y(df0, ps0, conf0)


if __name__ == '__main__':
    main()
