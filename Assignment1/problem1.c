#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>

double randomG();

double randomG(void)
{
    return (double) rand()/((double) RAND_MAX);
}


int main(argc, argv)
int argc;
char *argv[];
{
    int NOTRIALS=stoi(argv[3]);



    return 0;
}
