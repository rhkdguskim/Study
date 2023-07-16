#include <iostream>

using namespace std;

int testarry[] = {5,6,7,8,9,1,2,3,4,0};

void Swap(int *a, int *b)
{
    int temp = *b;
    *b = *a;
    *a = temp;
}

void SelectionSort(int a[])
{
    int indexmin;
    for(int i=0; i<10; i++) // 기능 3) 맨 처음에 위치를 뺀 나머지 배열을 같은 방법으로 교체합니다.
    {
        indexmin = i;
        // 기능 1) 주어진 배열 중 최소값을 찾는다.
        for(int j=i+1; j<10; j++)
        {
            if(a[indexmin] > a[j])
                indexmin = j;
        }
        // 기능 2) 그 값을 맨 앞에 위치한 값과 교체한다.
        Swap(&a[i], &a[indexmin]);
    }
}

int main(void)
{
    cout << "SelectionSort 전" << endl;
    for(int i=0; i<10; i++)
    {
        cout << testarry[i] << endl;
    }
    SelectionSort(testarry);
    cout << "SelectionSort 후" << endl;
    for(int i=0; i<10; i++)
    {
        cout << testarry[i] << endl;
    }

}

