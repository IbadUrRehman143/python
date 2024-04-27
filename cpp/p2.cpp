#include<iostream>
using namespace std;


int main(){
    int num = 1221;
    int num_ = num;

    int reverse = 0;
    while(num != 0){
        int digit = num%10;
        reverse = (reverse*10) + (digit);
        num /= 10;
    }
    if(num_ == reverse){
        cout << num << " is palindromen" << endl;
    }
    else{
        cout << num << " is not a palindrome" << endl;
    }
    return 0;
}
