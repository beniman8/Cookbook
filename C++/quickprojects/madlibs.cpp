// This is a mad libs program using C++

#include <iostream>
#include <string>

using namespace std;

void showLibs(){
    
    cout << "Yesterday, I decided to [verb 1] to the park with my [noun 1]."<<endl;
    cout <<"The weather was so [adjective 1] that we couldn't stop smiling!" <<endl;
    cout <<"Suddenly, a [adjective 2] [noun 2] appeared out of nowhere and started to [verb 2]." <<endl;
    cout <<"It was the strangest day ever!" <<endl;
}

void showLibs(string verb1,string verb2,string adjective1, string adjective2, string noun1, string noun2){

    cout << "Yesterday, I decided to "<< verb1 <<"  to the park with my"<< noun1 <<" ."<<endl;
    cout <<"The weather was so "<<adjective1  <<"  that we couldn't stop smiling!" <<endl;
    cout <<"Suddenly, a "<< adjective2<<" "<< noun2<<" appeared out of nowhere and started to "<< verb2 <<"." <<endl;
    cout <<"It was the strangest day ever!" <<endl;
}

int main(int argc, char const *argv[])
{

    showLibs();
    cout<<" "<<endl;

    string verb1,verb2,adjective1,adjective2,noun1,noun2;
    cout << "Enter a verb"<<endl;
    cin >>verb1;
    cout << "Enter a noun"<<endl;
    cin >>noun1;
    cout << "Enter a adjective"<<endl;
    cin >>adjective1;
    cout << "Enter a adjective"<<endl;
    cin >>adjective2;
    cout << "Enter a noun"<<endl;
    cin >>noun2;
    cout << "Enter a verb"<<endl;
    cin >>verb2;

    showLibs( verb1, verb2, adjective1, adjective2,  noun1,  noun2);

    
    return 0;
}
