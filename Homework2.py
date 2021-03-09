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
    print("The sum of the Fibonacci numbers smaller than your number is ", sumFib, ".")

def isPrime(num):
    lastNum = int(num**0.5)
    for i in range(2,(lastNum+1)):
        if num%i==0:
            print("Your number is not prime.")
            return
    print("Your number is prime.")

def Binary(decimal):
    #binary = [0]*8
    #for i in range(0,7):
    #    binary[(7-i)] = decimal%2
    #    decimal = int(decimal/2)
    binary = []
    while(decimal>0):
        binary.append([(decimal%2)])
        decimal = int(decimal/2)
    
    n = len(binary)
  
    print("The binary representation of your number is ", end="")
    for i in range(0,n): 
        print(binary[(n-1-i)], end="")
    print("\n")

def main():
    userInput = input("Please insert a positive number: ")
    while(1):
        if(userInput.isnumeric()):
            A = int(userInput)
            print("Here is some information about your number:)")
            Fibonacci(A)
            isPrime(A)
            Binary(A)
            return
        else:
            userInput = input("ERROR! Your input contains letters or special characters.\nPlease insert a valid number: ")
    
main()
