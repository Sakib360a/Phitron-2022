#include <iostream>
using namespace std;

class Mystack{
  public:

    int *a;
    int Stack_Size=0;
    int array_capacity;
    Mystack(){
        a= new int[1];
        array_capacity=1;
    }
    void increase_stack_capacity(){
        int *temp;
        temp = new int [array_capacity*2];
        for (int i = 0; i < array_capacity; i++)
        {
            temp[i]=a[i];
        }
        swap(temp,a);
        delete[] temp;
        array_capacity = array_capacity*2;
    }
    void PUSH(int value){
      if(Stack_Size<array_capacity){
        a[Stack_Size]=value;
         Stack_Size++;
      }
      else{
        increase_stack_capacity();
        a[Stack_Size]=value;
        Stack_Size++;
      }
    }
    void POP(){
      if(Stack_Size==0){
        cout<<"Stack is empty.";
      }
      else{
        cout<<"Popped: "<<a[Stack_Size-1]<<endl;
        Stack_Size--;
      }
    }
    void TOP(){
      if(Stack_Size==0){
        cout<<"Stack is empty.";
      }
      else{
       cout<<"Top element: "<< a[Stack_Size-1]<<endl;
      }
    }
};

int main()
{
  Mystack s;
  s.PUSH(15);
  s.PUSH(115);
  s.PUSH(1235);
  s.PUSH(5342);
  s.PUSH(554233);
  s.PUSH(5352);
  s.PUSH(5634);
  s.PUSH(52342);
  s.PUSH(55235);
  s.PUSH(55235);
  s.PUSH(5756);
  s.PUSH(6345);
  s.PUSH(524);
  s.PUSH(11435);
  s.PUSH(54355);
  s.PUSH(2342425);
  s.PUSH(52432);
  s.PUSH(11235);
  s.PUSH(454235);
  s.PUSH(32425);
  s.PUSH(5235);
  s.PUSH(52345);
  s.PUSH(53215);
  s.PUSH(654365);
  s.POP();
  s.TOP();
  s.POP();
  s.TOP();
  s.POP();
  s.TOP();
  return 0;
}