import sqlite3
import re

filePath = "input.sql" # 

checked = []

def checkPosition(k,l):
    data = '0'
    cont = True
    while(cont == True):
        l = l-1
        if(sqlStatements[k][l] not in ['1','2','3','4','5','6','7','8','9','0']):
            cont = False
    
    cont = True
    while(cont == True):
        l = l+1
        if(sqlStatements[k][l] in ['1','2','3','4','5','6','7','8','9','0']):
            data = data + sqlStatements[k][l]
            checked.append([k,l])
        else: cont = False
    values.append(data)

#********** MAIN CODE **********

# PASS THE SQL DATA INTO A DICCTIONARY
try:
    with open(filePath, "r") as file:
        sqlContent = file.read() #read the data in the file

        # Convertir los datos sql en una matriz
        sqlStatements = sqlContent.split('\n') #split the code
        sqlStatements = [statement.strip() for statement in sqlStatements if statement.strip()] #eliminate empty lines

        for i in range(0, len(sqlStatements), 1):
            sqlStatements[i] = sqlStatements[i].replace('',',').split(',')

        # Add empty row at the begining and at the end
        emptyRow = ['.'] * len(sqlStatements) # create empty row with 140 dots
        sqlStatements.insert(0, emptyRow)
        sqlStatements.insert(len(sqlStatements), emptyRow)

        i = 0
        j = 0
        auxList = []
        valid = False
        prevNum = False
        current = ''
        id = 0

        #********** FIND EVERY NUMBER NEXT TO A SYMBOL **********

        for stat in sqlStatements: # recorrer filas (i)
            for item in stat: # de cada fila recorrer columnas (j)
                if(item in ['1','2','3','4','5','6','7','8','9','0']): # ¿El item es un numero?
                    current = current + item # Agregar cifra al array
                    if(prevNum): # Is the previous item a number?
                        if(valid == True): # Era el anterior VALIDO?
                            if(sqlStatements[i][j+1] in ['1','2','3','4','5','6','7','8','9','0']): 
                                prevNum = True
                            else: prevNum = False
                        else: # Era el anterior NO VALIDO?
                            if(sqlStatements[i-1][j+1] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                                valid = True
                            if(sqlStatements[i+1][j+1] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                                valid = True
                            if(sqlStatements[i][j+1] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                                valid = True
                                prevNum = False
                            else:
                                if(sqlStatements[i][j+1] in ['1','2','3','4','5','6','7','8','9','0']): 
                                    prevNum = True # Is the next item a number?  
                                    auxList.append([i,j]) # Add the number to the auxiliary list.
                                else: prevNum = False

                    else: # El anterior no era un número
                        valid = False
                        # Comprobar lo que rodea al número
                        if(sqlStatements[i-1][j-1] not in ['1','2','3','4','5','6','7','8','9','0','','.']): 
                            valid = True
                        if(sqlStatements[i][j-1] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                            valid = True
                        if(sqlStatements[i+1][j-1] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                            valid = True
                        if(sqlStatements[i-1][j] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                            valid = True
                        if(sqlStatements[i+1][j] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                            valid = True
                        if(sqlStatements[i-1][j+1] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                            valid = True
                        if(sqlStatements[i+1][j+1] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                            valid = True
                        if(sqlStatements[i][j+1] not in ['1','2','3','4','5','6','7','8','9','0','','.'] and valid == False): 
                            valid = True
                        else:
                            if(sqlStatements[i][j+1] in ['1','2','3','4','5','6','7','8','9','0']): 
                                prevNum = True # Is the next item a number?
                                auxList.append([i,j]) # Add the number to the auxiliary list.
                    
                    # Resultados si el elemento era un numero
                    if (prevNum == False): # El siguiente no es numero
                        if(valid == False): # Y no ha dado valido
                            if(auxList != []):
                                for elem in auxList:
                                    sqlStatements[elem[0]][elem[1]] = '.'
                                    auxList = []
                            else: sqlStatements[i][j] = '.'
                            current = ''
                        else: # Si el ha dado válido
                            #print(id,'+',current,'=')
                            id += int(current)
                            #print(id)
                            current = '' 
                j += 1
            # cuando acaba de recorrese todas las columnas de la fila
            j = 0
            i += 1
        
        print("First answer is: ",id)

        #********** FIND EVERY VALID GEAR **********

        i = 0
        j = 0
        id2 = 0
        values = []

        for stat in sqlStatements: # recorrer filas (i)
            for item in stat: # de cada fila recorrer columnas (j)
                if(item=="*"):
                    #if([i-1,j-1] not in checked and sqlStatements[i-1][j-1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i-1,j-1)
                    #if([i,j-1] not in checked and sqlStatements[i][j-1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i,j-1) 
                    #if([i+1,j-1] not in checked and sqlStatements[i+1][j-1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i+1,j-1)
                    #if([i-1,j] not in checked and sqlStatements[i-1][j] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i-1,j)
                    #if([i+1,j] not in checked and sqlStatements[i+1][j] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i+1,j)
                    #if([i-1,j-1] not in checked and sqlStatements[i-1][j-1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i-1,j-1)
                    #if([i+1,j+1] not in checked and sqlStatements[i+1][j+1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i+1,j+1)
                    #if([i,j+1] not in checked and sqlStatements[i][j+1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i,j+1)

                    if(sqlStatements[i-1][j-1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i-1,j-1)
                    if(sqlStatements[i][j-1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i,j-1) 
                    if(sqlStatements[i+1][j-1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i+1,j-1)
                    if(sqlStatements[i-1][j] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i-1,j)
                    if(sqlStatements[i+1][j] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i+1,j)
                    if(sqlStatements[i-1][j-1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i-1,j-1)
                    if(sqlStatements[i+1][j+1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i+1,j+1)
                    if(sqlStatements[i][j+1] in ['1','2','3','4','5','6','7','8','9','0']): checkPosition(i,j+1)

                    if(len(values)==2): id2 += (int(values[0]) * int(values[1]))
                    values = []
                j += 1
            j = 0
            i += 1
        
        print("Second answer is: ",id2)
        
# error handling
except FileNotFoundError:
    print(f"The file '{filePath}' does not exist")
except Exception as e:
    print(f"An error ocurred: {e}")