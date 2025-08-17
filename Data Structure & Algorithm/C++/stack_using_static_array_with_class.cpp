#include<bits/stdc++.h>
using namespace std;

class Mystack{
  public:
    static const int MAX_SIZE = 500;
    int a[MAX_SIZE];
    int Stack_Size=0;
    
    void PUSH(int value){
      if(Stack_Size<MAX_SIZE){
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
  s.PUSH(5);
  s.TOP();
  s.PUSH(15);
  s.TOP();
  s.PUSH(25);
  s.TOP();
  s.POP();
   s.TOP();
   s.POP();
   s.TOP();
   s.POP();
   s.TOP();
  return 0;
}