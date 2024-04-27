#include<iostream>

using namespace std;
int main (){
    int num;
    cout << "enter a number";
    cin >> num;
    int factorial = 1;
    for (int i=1; i<num+1; i++){
        factorial *= i;

    }
    cout << " factorial is : "<< factorial << endl;
return 0 ;
}