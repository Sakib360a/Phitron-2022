#include <bits/stdc++.h>
using namespace std;
void push(int *arr, int &Stack_size, int size)
{
    int value = 0;
    cout << "Enter the Value you want to push: ";
    cin >> value;
    cout<<"\n";
    if (Stack_size < size)
    {
        Stack_size++;
        arr[Stack_size - 1] = value;
    }
    return;
}
void pop(int &Stack_size)
{
    if (Stack_size == 0)
    {
        cout << "Cannot pop, Stack is empty\n";
    }
    else
    {
        Stack_size--;
    }
    return;
}
void top(int *arr, int &Stack_size)
{
    if (Stack_size == 0)
    {
        cout << "Stack is empty.\n\n";
    }
    else
    {
        cout << "Top element: " << arr[Stack_size - 1]<<"\n\n";
    }
    return;
}
using namespace std;
int main()
{
    cout << "Stack using Static array in C++\n\n";
    int size = 50;
    int *arr = new int[size]();
    int Stack_size = 0;

    while (1)
    {
        cout << "Choose your operation: \n";
        cout << "1. Push\n";
        cout << "2. Pop\n";
        cout << "3. Top\n";
        cout << "4. Exit\n\n";
        int choice;
        cout<<"\n";
        cin >> choice;
        switch (choice)
        {
        case 1:
            push(arr, Stack_size, size);
            break;
        case 2:
            pop(Stack_size);
            break;
        case 3:
            top(arr, Stack_size);
            break;
        case 4:
            delete[] arr;
            return 0;
        default:
            cout << "Size of Stack Currently: " << Stack_size << "\n";
            cout<<endl;
            break;
        }
    }

    return 0;
}