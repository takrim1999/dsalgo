#include <stdio.h>
int maxmin(int arr[], int length, int *max, int *min);
int main()
{
    int max = NULL, min = NULL, array[] = {23, 87, 12, 6, 28, 35, 78, 108, 92, 56, 33};
    max = min = array[0];
    if (maxmin(array, sizeof(array) / sizeof(array[0]), &max, &min) == 0)
    {
        printf("maximum is: %d\n", max);
        printf("minimum is: %d\n", min);
    }
    else
        printf("Something went wrong");

    return 0;
}

int maxmin(int arr[], int length, int *max, int *min)
{
    for (int i = 0; i < length; i++)
    {
        // printf("%d\n", i);
        if (arr[i] > *max)
        {
            *max = arr[i];
        }
        if (arr[i] < *min)
        {
            *min = arr[i];
        }
    }
    return 0;
}