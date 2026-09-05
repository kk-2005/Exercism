
def is_armstrong_number(number):
    # Convert to string to find the number of digits (d) instantly
    num_str = str(number)
    d = len(num_str)
    
    # Calculate the sum using a generator expression inside sum()
    # It runs the power operation natively in C speed instead of explicit Python loops
    return number == sum(int(digit) ** d for digit in num_str)