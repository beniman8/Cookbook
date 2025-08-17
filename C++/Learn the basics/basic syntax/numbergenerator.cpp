

#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;


int main(int argc, char const *argv[])
{
    
    srand(time(NULL));
    int randomNumber = rand() %20;
    
    cout << randomNumber << endl;
    return 0;
}
