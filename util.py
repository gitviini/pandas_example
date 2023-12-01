import pandas as pd
import os

def clear() -> any:
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

#verify length datas in dataframe
def number(datalast=0,data=0) -> int:
        if datalast < data:
            return data
        else:
            return datalast

#create dataframe and return
def createDF(mode=0, data={}):
    match mode:
        case 0:
            #data if dictionary
            return pd.DataFrame(data) if data != {} else 'empty'
        case 1:
            #data is path
            return pd.read_csv(data)
        case _:
            name = input("name of dataframe:")
            #data is path
            return  pd.read_excel(data,sheet_name=name)
def show(tam=0,data={}) -> dict:
    for datas in data:
        tam = number(tam, len(data[datas])) 
        for datas in data:
            while len(data[datas]) < tam:
                data[datas].append('-')
    return data