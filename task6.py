def find_smallest_prime_digit(number):
    prime_digits = {'2', '3', '5', '7'}
    smallest_prime = None
    for digit in number:
        if digit in prime_digits:
            if smallest_prime is None or int(digit) < int(smallest_prime):
                smallest_prime = digit
    
    if smallest_prime is not None:
        return smallest_prime
    else:
        return "No prime digits found"
user_input = input("Enter the fingerprint number: ")
result = find_smallest_prime_digit(user_input)
print(result)

#==========================================================================================
#Programme to print the sum of odd digits in a number. { input : 2355 output : 13}

def sum_of_odd_digits(number):
    odd_sum = 0
    
    for digit in str(number):
        digit = int(digit)
        
        if digit % 2 != 0:
            odd_sum += digit
    
    return odd_sum

user_input = int(input("Enter a number: "))
result = sum_of_odd_digits(user_input)
print("Sum of odd digits:", result)

#==============================================================================================