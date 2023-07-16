#include <iostream>

using namespace std;

int testarr[] = {5,6,7,8,9,0,1,2,3,4}; // 배열 예제

void Swap(int* a, int* b)
{
    int temp = *b;
    *b = *a;
    *a = temp;
}

void BubbleSort(int *arr)
{
    for(int i=0; i < 10; i++)
    {
        for(int j=0; j<10-i; j++)
        {
            if(arr[j-1] > arr[j])
            {
                Swap(&arr[j-1], &arr[j]);
            }
        }
    }
}

int main()
{
    cout << "정렬 전 testarr" << endl;
    for(int i=0; i<10; i++)
    {
        cout << testarr[i] << endl;
    }

    BubbleSort(testarr);

    cout << "정렬 후 testarr" << endl;
    for(int i=0; i<10; i++)
    {
        cout << testarr[i] << endl;
    }
}