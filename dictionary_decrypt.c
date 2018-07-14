/* Brian Lee
 * 3620101
 * CMPSC 177
 * Brute-force dictionary attack
 * Compile using: gcc -lcrypt dictionary_decrypt.c -o dictionary_decrypt
 */

#define _XOPEN_SOURCE 

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if(argc != 3) {
    printf("Usage is %s hash salt\n", argv[0]);
    return 1;
  }
    //argv[1] is target hash, argv[2] is salt
    FILE *dictionary;
    char buffer[1000];
    char* hash;
    char* toHash;
    //int i = 1;
    
    dictionary = fopen("words.txt", "r");
    if(!dictionary)
    {
        return 1;
    }
    while(fgets(buffer, sizeof(buffer), dictionary) != NULL)
    {
        toHash = strtok(buffer, "\n");
        hash = crypt(toHash, argv[2]);
	//printf("Iteration: %s\n", i);
        if(strcmp(hash, argv[1]) == 0)
        {
            printf("Password: %s\n", toHash);
            return 0;
        }
	else
	  {
	    printf("Nope\n");
	  }
	//i++;
    }
    
    printf("No password found\n");
    
    return 0;
}
