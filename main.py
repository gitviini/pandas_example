import pandas as pd

def number(datalast=0,data=0):
        if datalast < data:
            return data
        else:
            return datalast

#create dataframe and return
def createDF(mode=0, data={}):
    match mode:
        case 0:
            #data if dictionary
            return pd.DataFrame(data)
        case 1:
            #data is path
            return pd.read_csv(data)
        case _:
            name = input("name of dataframe:")
            #data is path
            return  pd.read_excel(data,sheet_name=name)
            
while True:
    mode = int(input("""1)VIEW
2)NEW
3)EXIT
:"""))
    match mode:
        case 1:
            print(createDF(0,data))            
        case 2:
            print('NEW DATAFRAME:')
            data = {}
            name = input('name of column:')
            data[name] = []
            tam = 0
            while True:
                print(name)
                match int(input('1)NEW DATA\n2)NEW COLUMN\n3)EXIT\n:')):
                    case 1:
                        data[name].append(input('new data:'))
                    case 2:
                        name = input('new column:')
                        data[name] = []
                    case 3:
                        for datas in data:
                            tam = number(tam, len(data[datas])) 
                        for datas in data:
                            while len(data[datas]) < tam:
                                data[datas].append('-')
                        break
                    case _:
                        print('inválido')        
            print(createDF(0,data))
        case 3:
            break
        case _:
            print('inválido')

