from dataFile import  ConnectDB, IndexTable, CreateNewTable, CreateNewFile

def main():


    menu= int(input(".:Menu:.\n1-> Conectar a una base de datos.\n2-> Insertar datos.\n3-> Crear nueva tabla.\n4-> Salir\n\t ~>  "))

    if (menu == 1):
        print("***Ojo el nombre de la base de datos es como requerimiento que se alle en Capitalize")
        ConnectDB()
    elif (menu == 2):
        table_name= IndexTable()
        CreateNewFile(table_name)
    elif (menu == 3):
        print("***Ojo el nombre de la tabla va en Capitalize^^^\nLos filtros de la tabla tienen dos valores varchar para texto & Integer para numeros")
        table_name= IndexTable()
        CreateNewTable(table_name)
        # CreateNewTable(table_name)
    elif (menu == 4):
        exit()
    
while True:
    if main() == '__main__':
        main()