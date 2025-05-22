#include <stdio.h>

void bubble_sort(int array[], int size){
    int temp, i, j;
    for (i = 0; i < size - 1; i++)
    {
        for (j = 0; j < size - i - 1; j++)
        {
            if (array[j] > array[j+1])
            {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
            
        }
        
    }
    
}



int main(int argc, char const *argv[])
{
    int arr[] = {3,6,7,2,8};
    int size = sizeof(arr)/sizeof(arr[0]);

    bubble_sort(arr, size);

    for (size_t i = 0; i < size; i++)
    {
        printf("%d\n", arr[i]);
    }
    
    return 0;
}
