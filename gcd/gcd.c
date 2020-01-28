// Program to find the greatest common divisor between two numbers (Euclid's Algorithm)

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    // Get vars
    char ai[10], bi[10];

    // Get first number
    printf("Enter first number: ");
    scanf("%s", ai);

    // Get second number
    printf("End second number: ");
    scanf("%s", bi);

    // Check for numbers
    for (int c = 0; c < strlen(ai); c++)
    {
        if (!isdigit(ai[c]))
        {
            printf("Both inputs must be numbers.\n");
            return 1;
        }
    }
    for (int c = 0; c < strlen(bi); c++)
    {
        if (!isdigit(bi[c]))
        {
            printf("Both inputs must be numbers.\n");
            return 1;
        }
    }

    // Convert strings to ints
    int a = atoi(ai);
    int b = atoi(bi);

    // Find solution
    while (b != 0)
    {
        if (a > b)
        {
            a -= b;
        }
        else
        {
            b -= a;
        }
    }

    // Print solution
    printf("GCD: %i\n", a);

}
