#function for the half adder
def half_adder(a,b):
    #Half Adder: Adds two single binary digits. Takes 2 inputs and returns sum and carry.
    #Check if inputs are valid (0 or 1)
    if a not in [0, 1] or b not in [0, 1]: #(if a or b is not 0 or 1)
        print("Error: inputs must be 0 or 1") #print error message
        return None #return none
    
    sum_bit = a ^ b # XOR operation: sum is 1 only if inputs are different
    carry = a & b # AND operation: carry is 1 only if both inputs are 1
    return sum_bit, carry

def full_adder(a,b, carry_in):
    #Full Adder: Adds two binary digits plus a carry from previous addition. Takes 3 inputs (a, b, and carry from previous) and returns sum and carry.
    #Check if inputs are valid (0 or 1)
    if a not in [0, 1] or b not in [0, 1] or carry_in not in [0, 1]:#(if a or b is not 0 or 1)
        print("Error: inputs must be 0 or 1")#print error message
        return None #return none
    
    sum_bit = a ^ b ^ carry_in # XOR all three inputs for the sum bit

    carry_out = (a & b) | (b & carry_in) | (a & carry_in)   # Carry out is 1 if any two or more inputs are 1 (a AND b) OR (b AND carry_in) OR (a AND carry_in)
    
    return sum_bit, carry_out

# Test the functions

print("Half Adder Test (1 + 1):", half_adder(1, 1))
print("Full Adder Test (1 + 1 + 0):", full_adder(1, 1, 0))

def save_calculation(operation_type, inputs, result):
    #this function will save each calculation to a file
    with open("calculations.txt", "a") as file: #we open or create the file calculations.txt and append to it
        file.write(f"{operation_type}: inputs= {inputs}, result={result} \n ") #print out the operation type inputs and results
    

def load_calculations():
    #Load and displayu all saved calculations

    try:
        with open("calculations.txt","r") as file: # we try to open the file calculations.txt on read mode
            print("\n--- Saved Calculations ---")
            print(file.read()) #then print the contents of the files
    except FileNotFoundError: #if no file is found
        print("No saved calculations yet") # we print that no calculations has been done

def search_calculation(search_input):
    #Search for calculations by the input value
    try:
        with open("calculations.txt", "r") as file: #open calculations.txt
            lines=file.readlines()
            results = [] # create an empty list
            for line in lines: #for each line in the file 
                if str(search_input) in line: #we check to see if the search input is in the line
                    results.append(line) #if so we append it to the list
            if results: #if results has something inside
                print(f"\n--- Search Results for '{search_input}' ---")
                for result in results: # we print out the results
                    print(result.strip())
            else: # if nothing with the search input was found we print an error message
                print(f"No calculations found with the input {search_input}")
    except FileNotFoundError:
        print("No saved calculations found") # if no file is found we print out an error message sayign we dont have any calculations

def sort_calculations():
    # Sort and display all fo the calculations
    try:
        with open("calculations.txt", "r") as file: #try to open calculations.txt on read mode
            lines = sorted(file.readlines()) #we use the sorted function built in python which sorts the items in an ascending order
            print("\n--- Sorted Calculations ---")
            for line in lines:
                print(line.strip())  #prints the sorted version of the calculations.txt
    except FileNotFoundError:
        print("No saved calculations found") # if no saved calculations were found we print an error message