/*
we are going to print a bunch of stuff
*/

#include <iostream>
#include <string>


using namespace std;

int main(){
    string alpha="abcdefghijklmnopqrstuvewxyz";

    for (int i = 0; i < alpha.length(); i++)
    {
        
        cout << alpha[i] <<" " << int(alpha[i])<< endl;
    }
    
}