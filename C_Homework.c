#include <stdio.h>

int Fibonacci(int age)
{
    int currentFib = 1;
    int Fib2 = 1;
    int Fib3 = 0;
    int sum = 0 ;
    while (currentFib < age)
    {
        sum += currentFib;
        Fib3 = currentFib + Fib2;
        currentFib = Fib2;
        Fib2 = Fib3;
    }
    printf("The sum of all Fibonacci numbers smaller than your input is: %d\n", sum, "\n");
    return sum;
}

void Binary(int sum)
{
        int binary = 0;
	int n = 20;
        
	printf("The binary representation of this sum is:");
        for (n>=0; n--;)
	{
	(binary = sum>>n);
	if (binary & 1) 
	        printf ("1");
	else
		printf ("0");
        }
	printf ("\n");
}

int main(){
        int age;
	printf("Enter your age: ");
        scanf("%d", &age);
        Binary(Fibonacci(age));
        return age;
}

