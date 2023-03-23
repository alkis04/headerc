#include <stdio.h>

int test1(int a, int b){
    return a + b;
}

void test2(int a, int b){
    printf("%d\n", a + b);
}

char *test3(int a, int b){
    char *str = "Hello World";
    return str;
}

int **test4(int a, int b){
    int **p = (int **)malloc(sizeof(int *) * 2);
    p[0] = (int *)malloc(sizeof(int) * 2);
    p[1] = (int *)malloc(sizeof(int) * 2);
    p[0][0] = a;
    p[0][1] = b;
    p[1][0] = a + b;
    p[1][1] = a - b;
    return p;
}
