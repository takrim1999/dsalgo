#include <stdio.h>
#include <stdlib.h>
int *reverse_array(int *point, int length)
{
    int *new_array = (int *)malloc(sizeof(int) * length);
    printf("Reverse ");
    int j = 0;
    for (int i = length - 1; i >= 0; i--)
    {
        new_array[j] = *(point + i);
        j++;
    }
    point = new_array;
    return point;
}

void print(int *point, int length)
{
    // printf("%d", *point);
    printf("Array is:\n");
    for (int i = 0; i < length; i++)
    {
        printf("%d", *(point + i));
    }
    printf("\n");
}

int main()
{
    int array[6] = {1, 2, 3, 4, 5, 6};
    int *point = array;
    int length = sizeof(array) / sizeof(array[0]);
    print(point, length);
    print(reverse_array(point, length), length);
    return 0;
}