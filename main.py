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