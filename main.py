import pandas as pd

#verify length datas in dataframe
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
    try:
        print('\033[1;32m-PANDAS-\033[m')
        mode = int(input("""1)VIEW\n2)NEW\n3)EXIT\n:"""))
        match mode:
            case 1:
                print(createDF(0,data))            
            case 2:
                print('\033[1;34m-NEW DATAFRAME-\033[m')
                data = {}
                name = input('name of column:')
                data[name] = []
                tam = 0
                while True:
                    print('\033[1;34m-TABLE EDIT-\033[m')
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
    except Exception as erro: print(erro)
    finally: pass

