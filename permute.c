/* Brian Lee
 * 3620101
 * CMPSC 177
 * Find permutations of username
 * To compile: gcc permute.c -o permute
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(char *first, char *second)
{
    char temp;
    temp = *first;
    *first = *second;
    *second = temp;
}

void permutation(char *pass, int left, int right, FILE* file)
{
    int i;
    if (left == right)
    {
        printf("%s\n", pass);
        fprintf(file, "%s\n", pass);
    }
    else
    {
        for (i = left; i <= right; i++)
        {
            swap((pass + left), (pass + i));
            permutation(pass, left + 1, right, file);
            swap((pass + left), (pass+i));
        }
        
    }
}
 
/* Driver program to test above functions */
int main()
{
    FILE* permute;
    permute = fopen("permute.txt", "w");
    
    char str[] = "arya_stark";
    int n = strlen(str);
    permutation(str, 0, n - 1, permute);
    
    fclose(permute);
    return 0;
}