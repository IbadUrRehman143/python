#include<iostream>

//using namespace std;
using std::cout;
using std::endl;
using std::cin;

int factorial(int num){
    int fac = 1;
    for (int i = 1; i<=num; i++){
        fac *= i;
    }
    return fac;
}
int main(){
    int num;
    cout << "Enter a number: ";
    cin >> num;
    cout << factorial(num) << endl;
    return 0;
}
