/*
This is a guessing game made in c++
*/

#include <iostream>
#include <string>


using namespace std;

int main(){

    string secret_word ="secret";
    string guess;
    bool game = true;

    
    cout << "Here you will need to guess what is the secret word"<< endl;
    
    while (game)
    {
        
        cout << "What is the secret word? : "<< endl;
    
        cin >>  guess ;
        if (guess == secret_word)
        {
            cout << "you guess correctly the secret word is : " << secret_word << endl;
            game = false;
        }else{
            cout << "your guess is not correct"<< endl;
        }
        

    }
    


}