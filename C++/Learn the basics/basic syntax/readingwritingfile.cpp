#include <iostream>
#include <string>
#include <fstream>
#include <deque>


using namespace std;

template<typename T>
void print(T collection){
    print(collection,collection.size());
}

int main(int argc, char const *argv[])
{
    deque<string> foods = {"carrot","ice cream","beans"};

    ofstream feeds("foods.txt");

    // writint multiple line of code in a file
    for (string food : foods)
    {
        feeds << food << endl;
    }

    //reading multiple lines of code 
    ifstream feed("foods.txt");
    string food;
    while (feed >> food)
    {
        foods.push_back(food);
    }
    
    
    

    cout  << "what its your name"<<endl;
    string item;
    cin >> item;

    ofstream file("items.txt");
    file << item;
    file.close();
    
    ifstream files("items.txt");
    string items;
    files >> items;

    cout << "coooooooooll "<<items<<endl;
    files.close();
    system("pause");
    return 0;
}
