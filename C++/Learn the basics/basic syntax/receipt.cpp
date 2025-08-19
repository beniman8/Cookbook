#include <iostream>
#include <string>
#include <array>
#include <vector>

using namespace std;


void printArray(string items[], int size){

    for (int i = 0; i < size; i++)
    {
        cout << items[i] << endl;

    }
    
}

void printSTDArray(array<string,5> items){
    for (int i = 0; i < items.size(); i++)
    {
        cout << items[i] << endl;
    }
    
}


void printVector(vector<string> items){
    
    for (int i = 0; i < items.size(); i++)
    {
        cout << items[i] << endl;
    }
}

int main(int argc, char const *argv[])
{
    string foods[3]={"grapes","carrots","water mellon"};

    array<string,5> cookies={"chocolate","vanilla","pink","green","red"};

    vector<string> random={"hot","cold","green","sun","mon"};
    random.push_back("lol");



    printArray(foods,sizeof(foods)/sizeof(foods[0]));
    printSTDArray(cookies);
    printVector(random);


  /*

    for (int i = 0; i < 3; i++)
    {
        cout << cookies[i] << endl;
        cout << foods[i] << endl;
    }
    
    for (auto food : foods)
    {
        cout << food << endl;

    }
    

  */  

    




    system("pause");
    return 0;
}

