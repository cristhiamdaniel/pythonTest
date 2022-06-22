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