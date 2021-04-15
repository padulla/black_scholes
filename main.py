#!usr/bin/env python3
import numpy as np
import pandas as pd


import sys
sys.path.append('C:\\Users\\leand\\OneDrive\\Documentos\\GitHub\\padulla\\black_scholes')

from utils import *
import Call
import Put

FIXED_RATE =  -3.863/ 100   #3.40 / 100 
NOTIONAL = - 50_000_000

def main():
    data = pd.read_excel("C:\\Users\\leand\\OneDrive\\Documentos\\GitHub\\padulla\\black_scholes\\Pasta1.xlsx", header = 1,engine='openpyxl').iloc[0]
    params = excel.extract_option_params_from_excel(data, FIXED_RATE)

    #c = Call.Call(**params)
    p = Put.Put(**params)
    print(params)
    print("Delta = {:,.2f}".format(p.delta()))
    print("Gamma = {:,.2f}".format(p.gamma()))
    print("$Gamma_v2 = {:,.2f}".format(p.dollar_gamma(p.S)))
    print("$Gamma = {:,.2f}".format(p.dollar_gamma(NOTIONAL)))


if __name__ == "__main__": main()



