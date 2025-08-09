#include <bits/stdc++.h>
using namespace std;
int Size = 50,Stack_Size=0;
int *Stack = new int[Size]();
void push(int value)
{
    if(Stack_Size>Size)
    {
        cout<<"Cannot push, Stack is full."<<endl;
    }
    else{
        Stack_Size++;
        Stack[Stack_Size-1]=value;
    }

}
void pop()
{
    if(Stack_Size==0)
    {
        cout<<"Cannot pop, Stack is empty."<<endl;
    }
    else{
        Stack_Size--;
    }
}
void top()
{
    if(Stack_Size==0)
    {
        cout<<"Stack is empty."<<endl;
    }
    else{
        cout<<"Top element: "<<Stack[Stack_Size-1]<<endl;
    }
}
int main()
{
    push(5);
    //pop();
    push(7);
    top();
    return 0;
}