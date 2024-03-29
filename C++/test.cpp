#include <iostream>
using namespace std;

bool isPrime(int n){
    for(int i=2;i<n;i++){

        if(n%i==0)
            return false;
    }

    return true;
}

int main(){

    if(isPrime(104729))
        cout << "Prime";
    else
        cout << "Not Prime";
    return 0;
}