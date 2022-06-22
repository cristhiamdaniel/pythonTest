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