def Fibonacci(userAge):
    currentFib = 1
    Fib2 = 1
    Fib3 = 0
    sumFib = 0 
    while (currentFib < userAge):
        sumFib += currentFib
        Fib3 = currentFib + Fib2
        currentFib = Fib2
        Fib2 = Fib3
    print("The sum of the Fibonacci numbers smaller than your input is ", sumFib)

def isPrime(num):
    lastNum = int(num**0.5)
    for i in range(2,(lastNum+1)):
        if num%i==0:
            print("The inserted number is not prime")
            return
    print("The inserted number is prime")

def Binary(decimal):
    binary = [0]*8
    for i in range(0,7):
        binary[(7-i)] = decimal%2
        decimal = int(decimal/2)
    print("The binary representation of your number is ", end="")
    for i in range(0,8): 
        print(binary[i], end="")
    print("\n")

def main():
    A = int(input("Please insert a number"))
    Fibonacci(A)
    isPrime(A)
    Binary(A)

main()
