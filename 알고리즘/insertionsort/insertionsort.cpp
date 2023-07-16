#include <iostream>
int testarr[] = {5,6,7,8,9,1,2,3,4,0};

using namespace std;

void insertionsort(int arr[])
{
    int prev, temp;
    for(int i=1; i<10; i++)
    {
        prev = i - 1;
        temp = arr[i];
        while((arr[prev] > temp) && prev >= 0 )
        {
            arr[prev+1] = arr[prev];
            prev--;
        }
        arr[prev + 1] = temp;
    }
}

int main()
{
    cout << "삽입 정렬 전" << endl;

    for(int i=0; i<10; i++)
    {
        cout << testarr[i] << endl;
    }

    insertionsort(testarr);

    cout << "삽입 정렬 후" << endl;
    for(int i=0; i<10; i++)
    {
        cout << testarr[i] << endl;
    }
}