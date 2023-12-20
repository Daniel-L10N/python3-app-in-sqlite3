from sqlite3 import connect

def ConnectDB():
    nameDB= str(input("Ingrese el nombre de la Base de Datos: "))
    
    global cursor
    global connecxionDB

    #Conexion a la base de datos
    connecxionDB = connect(nameDB.capitalize())
    cursor= connecxionDB.cursor()

    return None

def IndexTable():
    table_name= str(input("Ingrese el nombre de la tabla: "))
    return table_name.capitalize()
    

    

def CreateNewTable(table_name):
    
    num_columns= int(input("Ingrese el numero de columnas: "))
    columns= []
    for i in range(num_columns):
        def ExtructureTable():
            column_name= str(input(f"Ingrese el nombre de la columna {i+1}: ")).capitalize()
            type= str(input(f"Selecione el tipo de dato para {column_name}\n1- Texto\n2-Numerico\n3-Repetir\n~>  "))
            if type == '1':
                data_type ="VARCHAR"
            elif type == '2':
                data_type = "INTEGER"
            elif type == '3':
                ExtructureTable()
            else:
                print("Error, Obcion no valida, intentelo nuevamente")
                ExtructureTable()
            data= f"{column_name} {data_type}"
            return data
        columns.append(ExtructureTable())
    
    
    
    #Create Table
    create_table_query= f"CREATE TABLE {table_name} ({','.join(columns)})"
    cursor.execute(create_table_query)
    # corsor.execute(f"CREATE TABLE {table_name} ({','.join(columns)})") #Otra alternativa
    #guardando cambios y cerrando la connexion
    connecxionDB.commit()
    connecxionDB.close()
    print(f"\t^^^^^^La tabla {table_name} ha sido creada exitosamente!!!")
    return num_columns



def CreateNewFile(tableName):
    num_data= int(input("Digite el numero de datos a ingresar por cada fila en dicha tabla: "))
    alldata, addData= [], []
    def AddDatalista():
        for i in range(num_data):
            addData.append(input(f"Dato #{i}~> "))
        alldata.append(addData)
        menu= str(input("Precione Q para continuar & enter para seguir ingresando valores: "))
        if menu == 'q' or 'Q':
            pass
        elif menu == '':
            AddDatalista()
        else:
            print("Error, obcion no valida, continuamos.")
            pass
    #insert data into the table
    query = f"INSERT INTO {tableName} VALUES("
    for i in range(num_data):
        query += '?'
        if i < (num_data -1):
            query += ','
    query += ')'
    cursor.execute(query, alldata)
    #Commit the changes and close the connection
    connecxionDB.commit()
    connecxionDB.close()

