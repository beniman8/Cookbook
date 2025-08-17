

#include <iostream>
#include <string>


using namespace std;

int main(){

    cout << "Do you want to play a game (y/n) ? : "<< endl;
    string response;

    cin >> response;

    cout << "You have answered " <<  response << endl;

    if (tolower(response[0]) == 'y')
    {
        cout << " YES" << endl;
    }else{
        cout << " NO" << endl;

    }
    


    system("pause");
    return 0;
}