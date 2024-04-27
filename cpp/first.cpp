#include<iostream>

using namespace std;
int main(){
    int num;
    cout << "Enter a number of which you want to find factorial: ";
    cin >> num;
    int factorial = 1;
    for (int i=1; i<num+1; i++){
        factorial *= i;
    }
    cout << "Factorial is: " << factorial << endl;
    return 0;
}