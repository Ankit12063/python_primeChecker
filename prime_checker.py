# Program to check if a number is prime or not

num = 407

# uncomment this to enable input from user
#num = int(input("Please input an integer :)"))


# prime numbers are greater than 1
def is_prime(num):
    """
    check whether a number is prime or not.
    we iterate over all numbers between 2 and the sqrt of num
    (and not until num, to make it more efficient since no factor
    of num can be greater than the sqrt of num)

    :param num: number to check if its prime
    :type num: int
    """
    if num > 1:
       # check for factors
       for i in range(2, int(num** (1/2)) + 1):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,"is not a prime number")

is_prime(num)
