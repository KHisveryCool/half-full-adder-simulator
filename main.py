#function for the half adder
def half_adder(a,b):
    sum_bit = a ^ b #sum bit will be using an XOR Operation to use this in python we do ^
    carry = a & b #the carry operation checks to see if both the variables are true if so the result is true
    return sum_bit, carry

def full_adder(a,b, carry_in):
    