def get_prime_factors(number): # create function to get the prime factors of numbers
    factors = [] # Create list of the factors so we can pull
    divisor = 2 # divisor var 
    while divisor <= number: # 2 <= everthing above 2
        if number%divisor == 0: # first find if the number is divisible by 2
            factors.append(divisor) # if it is append that the divors
            number = number // divisor
        else: 
            divisor += 1
    return factors


# commands used in solution video for reference

if __name__ == '__main__':
    print(get_prime_factors(3232))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
