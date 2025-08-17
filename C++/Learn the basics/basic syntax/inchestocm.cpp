#include <iostream>

using namespace std;

int main(){

    const float factor = 2.54; // 1 inch equals 2.54 cm
    float x,in,cm;
    char ch =0;
    cout << "enter length: " << endl;
    
    cin >>x; // read floating point

    cout << "enter i for inches and c for centimeter: " << endl;
    cin >> ch;

    switch (ch)
    {
    case 'i':
        in = x;
        cm = x*factor;
        break;
    
    case 'c':
        in = x/factor;
        cm = x;

        break;
    
    default:
        in = cm = 0;
        break;
    }
    cout << in << " in = " << cm <<" cm\n";
}