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
    
    #Test cases I will change this later
    result = half_adder(1,1)
    print("Half Adder Test(1,1)", result)
    save_calculation("Half Adder", (1,1),result)

    #note add an error handling code after
    result = full_adder(1, 1, 0)
    print("Full Adder Test (1 + 1 + 0):", result)
    save_calculation("Full Adder", (1, 1, 0), result)

def load_calculations():
    #Load and displayu all saved calculations

    try:
        with open("calculations.txt","r") as file: # we try to open the file calculations.txt on read mode
            print("\n--- Saved Calculations ---")
            print(file.read()) #then print the contents of the files
    except FileNotFoundError: #if no file is found
        print("No saved calculations yet") # we print that no calculations has been done

load_calculations()