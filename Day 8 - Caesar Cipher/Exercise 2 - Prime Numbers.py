def check_prime(num):

    if num == 1:
        print("It's not a prime number.")
        return

    for i in range(2, num):
        if num % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")
    
check_prime(int(input("")))