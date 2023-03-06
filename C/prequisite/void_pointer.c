#include <stdio.h>
int main()
{
    int n = 10;
    void *pointer = &n;              // pointer is a void pointer here. It does not contain any type but can be initialized by any type
    printf("%d\n", *(int *)pointer); // this is called type casting, we are type casting to integer to print a value
    // printf("%c\n",*(int*)pointer);
    return 0;
}