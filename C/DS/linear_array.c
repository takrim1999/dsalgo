#include <stdio.h>

void print_array(int size, int *a)
{
    // printf("%d", *a);

    for (int i = 0; i < size; i++)
    {
        printf("%d,", *(a + i));
    }
    printf("\n");
}

int main()
{
    int array[] = {1, 2, 3};
    int length = (sizeof(array) / sizeof(array[0]));
    int *a;
    a = array;
    print_array(length, a);

    return 0;
}