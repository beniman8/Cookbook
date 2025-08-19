#include <iostream>
#include <string>
#include <array>
#include <vector>


using namespace std ;


template<typename T> // some type we will call template T

void print(T collection,int size){

    for (int i = 0; i < size; i++)
    {
        cout << collection[i] << endl;
    }
    
}

template<typename T>
void print(T collection){
    print(collection,collection.size());
}


int main(int argc, char const *argv[])
{
    string foods[3]={"grapes","carrots","water mellon"};

    array<string,5> cookies={"chocolate","vanilla","pink","green","red"};

    vector<string> random={"hot","cold","green","sun","mon"};
    random.push_back("lol");

    print(foods,3);
    print(cookies);
    return 0;
}
