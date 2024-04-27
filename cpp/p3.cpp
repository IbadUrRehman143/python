#include<iostream>
using namespace std;
int main(){

    int year,prev=0;
    cin>>year;
    if(year%4==0){
        cout<<"leap year"<<endl;
        for(int i=0;i<10;i++){
            year=year-4;
            cout<<"previous"<<year<<endl;
        }

    }
    else{
        cout<<"not leap year";
    }

return 0;}
