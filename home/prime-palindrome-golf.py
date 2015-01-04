def isPrime(number):
    if number == 2:
        return True
    if number%2 == 0:
        return False
    for i in range(3, number/2, 2):
        if number%i == 0:
            return False
    return True

def isPalindrome(number):
    return str(number) == str(number)[::-1]

def golf(number):
    i = number
    while 1:
        i+=1
        if isPalindrome(i) and isPrime(i):
            return i
    return number + 1
