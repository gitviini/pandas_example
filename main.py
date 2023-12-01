
from time import sleep
from util import *

#data global
data = {}
            
while True:
    clear()
    try:
        print('\033[1;32m-PANDAS-\033[m')
        mode = int(input("""1)VIEW\n2)NEW\n3)EXIT\n:"""))
        match mode:
            case 1:
                
                print(createDF(0,data))
            case 2:
                print('\033[1;34m-NEW DATAFRAME-\033[m')
                name = input('name of column:')
                data[name] = []
                tam = 0
                while True:
                    clear()
                    print(f'\033[1;34m-TABLE {name} EDIT-\033[m')
                    print(data)
                    match int(input('\n1)NEW DATA\n2)NEW COLUMN\n3)EXIT\n:')):
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
                            print('\033[0;31minvalid\033[m')
                print(createDF(0,data))
                sleep(2)
            case 3:
                break
            case _:
                print('\033[0;31minvalid\033[m')
    except: print('\033[0;31minvalid\033[m')
    finally: sleep(2)

