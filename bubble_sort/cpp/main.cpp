#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

void bubble_sort(std::vector<int>& array){
    bool swaped;
    int temp, i, j;
    for (i = 0; i < array.size() - 1; i++)
    {
        for (j = 0; j < array.size() - i - 1; j++)
        {
            if (array[j] > array[j+1])
            {
                std::swap(array[j], array[j+1]);
            }
            
        }
        
    }
    
}



int main(int argc, char const *argv[])
{
    std::vector<int> arr = {3,6,7,2,8};

    bubble_sort(arr);

    for (const auto& num: arr)
    {
        std::cout << num << '\n';
    }
    
    return 0;
}
