import sqlite3
import re

filePath = "input.sql" # 

#********** MAIN CODE **********

# PASS THE SQL DATA INTO A DICCTIONARY

ex = [12,13,14]

try:
    with open(filePath, "r") as file:
        sqlContent = file.read() #read the data in the file
        sqlContent = sqlContent.replace("Game", '')
        sqlContent = sqlContent.replace("red", 'r')
        sqlContent = sqlContent.replace("green", 'g')
        sqlContent = sqlContent.replace("blue", 'b')
        sqlContent = sqlContent.replace(':','\n')
        sqlStatements = sqlContent.split('\n') #split the code
        sqlStatements = [statement.strip() for statement in sqlStatements if statement.strip()] #eliminate empty lines
        #print(sqlStatements)

        subarrays = []
        for i in range(0, len(sqlStatements), 2):
            subarray = sqlStatements[i:i+2]
            subarrays.append(subarray)
        #print(subarrays)

        #Crear el diccionario
        dic = {}
        for key, value in subarrays:
            #Prepare values
            
            aux = value.split(';')

            i=0
            for e in aux:
                # Detectar si existen todos los datos
                if(e.count('g')==0):
                    e=e+",0g" #add g
                if(e.count('r')==0):
                    e=e+",0r" #add r
                if(e.count('b')==0):
                    e=e+",0b" #add b
                e = e.split(",")

                # Reorder rgb
                j = 0
                for n in e:
                    n = n.split(' ')
                    if(n.count('r')>0):
                        r = [re.sub(r'[^0-9]', '', element) for element in n]
                        r = [statement.strip() for statement in r if statement.strip()] #eliminate empty lines
                        r = r[0]
                    if(n.count('g')>0): 
                        g = [re.sub(r'[^0-9]', '', element) for element in n] 
                        g = [statement.strip() for statement in g if statement.strip()] #eliminate empty lines
                        g = g[0]
                    if(n.count('b')>0): 
                        b = [re.sub(r'[^0-9]', '', element) for element in n]
                        b = [statement.strip() for statement in b if statement.strip()] #eliminate empty lines
                        b = b[0]
                    j+=1
                temp = []
                temp.append(r)
                temp.append(g)
                temp.append(b)
                r = 0
                g = 0
                b = 0

                aux[i] = temp # Save temp as aux
                i+=1
            
            dic[key] = aux # Save aux as value of the dictionary key

        id1 = 0
        for key,value in dic.items():
            #print(f"{key}: {value}")
            pasable = True
            for v in value:
                #print(v)
                if(int(v[0])<=ex[0] and int(v[1])<=ex[1] and int(v[2])<=ex[2]): continue
                else: pasable = False
            if(pasable): 
                #print(key + " Pasable")
                id1 += int(key)
            #else: print(key + " No Pasable")
        #print("FIRST ANSWER: ",id1)

        id2 = 0
        for key,value in dic.items():
            maxR = 0 
            maxG = 0 
            maxB = 0
            for v in value:
                print(v)
                if(int(v[0])!=0 and maxR<int(v[0])): 
                    maxR = int(v[0])
                if(int(v[1])!=0 and maxG<int(v[1])): 
                    maxG = int(v[1])
                if(int(v[2])!=0 and maxB<int(v[2])):
                    maxB = int(v[2])
            print("Max R: ", maxR," Max G: ",maxG," Max B: ",maxB)
            potencia = maxR*maxG*maxB
            print(potencia)
            id2 += potencia
            print("________________")
        print("SECOND ANSWER: ",id2)
        
# error handling
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist")
except Exception as e:
    print(f"An error ocurred: {e}")