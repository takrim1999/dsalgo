#include <stdio.h>

void reverse_array(int *point, int length)
{
    // printf("%d", *point);
    length--;
    for (int i = length; i >= 0; i--)
    {
        printf("%d", *(point + i));
    }
}

int main()
{
    int array[4] = {1, 2, 3, 4};
    int *point = array;
    int length = sizeof(array) / sizeof(array[0]);
    reverse_array(point, length);
    return 0;
}