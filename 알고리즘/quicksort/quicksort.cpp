#include <iostream>

void solve()
{
    int array[] = { 80, 70, 60, 50, 40, 30, 20 };
    quickSort(array,0, sizeof(array)/sizeof(int) - 1);
    
}
void swap(int array[], int a, int b)
{
    int temp = array[b];
    array[b] = array[a];
    array[a] = temp;
}


int partition(int array[], int left, int right)
{
    int pivot = array[left];
    int i = left, j = right;

    while(i < j)
    {
        while(pivot < array[j])
        {
            j--;
        }
        while(i<j && pivot >= array[i])
        {
            i++;
        }
        swap(array, i, j);
    }
    array[left] = array[i];
    array[i] = pivot;

    return i;
}

void quickSort(int array[], int left, int right)
{
    if(left >= right)   return;

    int pi = partition(array, left, right);

    quickSort(array, left, pi-1);
    quickSort(array, pi+1, right);
}