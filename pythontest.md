# Python Test
**Nombre** : Cristhiam Daniel Campos Julca
**Date**: June 22nd, 2022

## Problem 1: A valid postal code
File: ```problem1.py```

```py
import re

while True:
    # Postal Code
    P = input("Type a postal code:\n")
    ### Regular Expressions ###
    # P must be a number in the range from 10.0000 to 1.000.000 inclusive.
    regex_integer_in_range = re.compile("^([2-8][0-9][0-9][0-9][0-9]|1[1-9][0-9][0-9][0-9]|10[1-9][0-9][0-9]|100[1-9][0-9]|1000[0-9]|9[0-8][0-9][0-9][0-9]|99[0-8][0-9][0-9]|999[0-8][0-9]|9999[0-9]|[2-8][0-9][0-9][0-9][0-9][0-9]|1[1-9][0-9][0-9][0-9][0-9]|10[1-9][0-9][0-9][0-9]|100[1-9][0-9][0-9]|1000[1-9][0-9]|10000[0-9]|9[0-8][0-9][0-9][0-9][0-9]|99[0-8][0-9][0-9][0-9]|999[0-8][0-9][0-9]|9999[0-8][0-9]|99999[0-9]|1000000)$")
        
    # P must not contain more than one alternating repetitive digit pair.
    regex_alternating_repetitive_digit_pair = re.compile(r"(\d)(?=\d\1)")
    
    print("###############################")
    # Print the input value
    
    print("The input postal code is %s" %(P))
    print("Is the code valid?", (bool(re.match(regex_integer_in_range,P)) and len(re.findall(regex_alternating_repetitive_digit_pair,P))<2))

    # Ask for next iteration

    nextInput = input("Do you want to continue? (Y/N) ")

    # Terminate from the loop if 'n' is pressed

    if nextInput.upper() == 'N':

        break

# Print the termination message

print("Program terminated.")
```
The output from the terminal is:
```bash
Type a postal code:
110000
###############################
The input postal code is 110000
Is the code valid? False
Do you want to continue? (Y/N) y
Type a postal code:
121426
###############################
The input postal code is 121426
Is the code valid? True
Do you want to continue? (Y/N) n
Program terminated.
```
## Problem 2: Let's use decorators to build a name directory!
File: ```problem2.py```

```py
import operator

N = int(input('Enter the number of people: '))

if N >= 1 and N <= 10: # Constraints
    
    peopleList = []
    key_list = ['title', 'name', 'lastname', 'age', 'gender']
    value_list = []
    
    for i in range(N):
        n = input("Enter your first name, last name, age and gender separated by space: ").title()
        value_list = n.split()
        
        '''Validating that the information entered is correct'''
        if len(value_list) == 4:
            
            '''Entering the title according to the gender of the person'''
            if value_list[-1] == 'M':
                value_list.insert(0,"Mr.")
            else:
                value_list.insert(0,"Ms.")
                
            dict_from_list = dict(zip(key_list, value_list))
            peopleList.append(dict_from_list)
        
        else:
            print("The data was entered incorrectly")
            break
        
else:
    print("The number of people is not allowed. It's out of range")
    
    
# We order the list according to the age of the people
sortedList = sorted(peopleList, key=operator.itemgetter('age'))

'''
In the final list the information of the people is stored (title, name and surname) 
organized in ascending order according to their age.
'''
finalList = []
for x in range(len(sortedList)):
    line = sortedList[x].get('title') + " " + \
            sortedList[x].get('name') + " " + \
            sortedList[x].get('lastname')
    finalList.append(line)


print("############################################")
print(N)
for i in finalList:
    print(i)
```

The output from the terminal is:
```bash
Enter the number of people: 3
Enter your first name, last name, age and gender separated by space: Mike Thomson 20 M
Enter your first name, last name, age and gender separated by space: Robert Bustle 32 M
Enter your first name, last name, age and gender separated by space: Andria Bustle 30 F
############################################
3
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
```
## Problem 3: Valid email
File: ```problem3.py```

```py
# Input
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
#############################################################
localNames = []
domainNames = []

''' Program validations '''
if 1<=len(emails)<=100:
  for email in emails:
    try:
      indice = email.index('@')

      if 1<=len(email)<=100:
        localEmail = email[:indice]
        dominioEmail = email[indice:]
          
        if len(localEmail) != 0 and len(dominioEmail) != 0:
          localNames.append(localEmail)
          domainNames.append(dominioEmail)
        else:
          print("empty local field name")
      else:
        print("Email character limit exceeded")
    except:
      print("Some email does not contain the @ character")
else:
  print("Mailing list exceeds limit")

for locales in localNames:
  if locales[0] == "+":
    break
for dominios in domainNames:
  if dominios[-4:] != '.com':
    break

def validatedEmails(emails):
    
    listaNombre_nueva = []
    listaDominio_nueva = []
    for elemento in localNames:
        e = elemento.lower()
        characters = "."
        for x in range(len(characters)):
            local = e.replace(characters[x],"")  

        letra = '+'
        if letra in local:
            indicenuevo = local.index('+')
            localnuevo =  local[:indicenuevo]
            listaNombre_nueva.append(localnuevo)
        else:
            listaNombre_nueva.append(local)
    
    for elemento in domainNames:
        e = elemento.lower()
        listaDominio_nueva.append(e)

    listafinal = []
    for i in range(len(listaNombre_nueva)):
        x = listaNombre_nueva[i] + listaDominio_nueva[i]
        listafinal.append(x)

    resultantList = []
     
    for element in listafinal:
        if element not in resultantList:
            resultantList.append(element)
        
    return len(resultantList)

# Output
a = validatedEmails(emails)
print(a)
```
The output from the terminal is:
```bash
3
```
## Problem 4: Optimize is_prime

File ```problem4.py```

```py
import math
def is_prime_fast(number):
  if number <= 1 or (number > 2 and number % 2 == 0):
    return False
  else:
    for factor in range(2,int(math.sqrt(number))+1):
      if number % factor == 0:
        return False
    
  return True

def is_prime(n):
    max = int(math.sqrt(n))
    if  n == 2:
        return True
    elif n % 2 == 0 and n >= 2:
        return False
    elif n == 1:
        return False
    for x in range(3, max+1, 2):
        if n % x == 0:
            return False
    return True

for n in range(2,100):
  assert is_prime(n) == is_prime_fast(n)
```
In notebook:
```py
%%timeit
is_prime(67867967)
```
output:
```bash
1000 loops, best of 5: 335 µs per loop
```
```py
%%timeit
is_prime_fast(67867967)
```
output:
```bash
1000 loops, best of 5: 673 µs per loop
```

