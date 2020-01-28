// Program to find the next prime number after a given input

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(void)
{

    // Get vars
    char ai[10];
    int prime = 0;

    // Ask for input
    printf("Number: ");
    scanf("%s", ai);

    // Check for number
    for (int c = 0; c < strlen(ai); c++)
    {
        if (!isdigit(ai[c]))
        {
            printf("Invalid input\n");
            return 1;
        }
    }

    // Convert to int
    unsigned int a = atoi(ai);

    // Loop to increment the number
    while (prime == 0)
    {
        // Find the prime
        for (unsigned int c = 2; c <= a; c++)
        {
            // Check to see if it mods by current number and that it isn't itself
            if (a % c == 0 && a != c)
            {
                // Break out to the next number
                break;
            }
            else if (a == c)
            {
                // Found it
                printf("Next prime: %i\n", a);
                prime = 1;
                return 0;
            }
        }
        // Increment the search number
        ++a;
    }
}