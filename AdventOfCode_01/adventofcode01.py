import sqlite3
import re

filePath = "input.sql"

#********** EXTRACT NUMBERS AND WORDS THAT REPRESENT NUMBERS **********
def extractNumbers(inputString):
    pattern = re.compile('one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9', re.IGNORECASE)
    #pattern = re.compile(r'\d') # r'\d+' encuentra los numeros
    matches = re.findall(pattern, inputString)
    return matches

#********** REPLACE WORDS WITH NUMBERS **********
def ReplaceNumberWordsWithNums(array):
    # Dictionary mapping numbers to numeric values
    wordToNumber = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 
                     'ten': '10'}
    pattern = re.compile(r'(?:'+'|'.join(wordToNumber.keys())+r')',re.IGNORECASE)
    replacedArray = [re.sub(pattern, lambda x: wordToNumber[x.group().lower()], element) for element in array]
    return replacedArray

#********** REMOVE NON-NUMERIC CHARACTERS **********
def extractNumbersOnly(array):
    cleanedArray = [re.sub(r'[^0-9]', '', element) for element in array] 
    return cleanedArray

#********** MAIN CODE **********
try:
    with open(filePath, "r") as file:
        sqlContent = file.read() #read the data in the file
        sqlStatements = sqlContent.split('\n') #split the code
        sqlStatements = [statement.strip() for statement in sqlStatements if statement.strip()] #eliminate empty lines
        print(len(sqlStatements))
        code = 0
        i = 0
        for s in sqlStatements:
            print(s)
            validElements = extractNumbers(s)
            print(validElements)
            onlyNum = ReplaceNumberWordsWithNums(validElements)
            print(onlyNum)
            value = int(onlyNum[0] + (onlyNum[len(onlyNum)-1]))
            print(value)
            code += value
            print(code)
            i+=1
            value = 0
        print(i)
# error handling
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist")
except Exception as e:
    print(f"An error ocurred: {e}")