#include <iostream>
#include <string>
#include <deque>
#include <fstream>


using namespace std;



class Food{
    public:
    string name;
    double cost;
    
    void print(){
        cout << name <<" " << cost<< endl;
    }
    static void printFoods(deque<Food> foods){
        for (Food food: foods)
        {
            food.print();
        }
        
    }

    static deque<Food> readFoods()
    {
        deque<Food> savedFoods;
        ifstream files("foods.txt");
        string name;
        double cost;
        while (files >> name >> cost)
        {
            savedFoods.push_back(Food(name,cost));
        }

        files.close();
        return savedFoods;
        

    }

    static void readFoods(deque<Food> &foods){
        ifstream files("foods.txt");
        string name;
        double cost;
        while (files >> name >> cost)
        {
            foods.push_back(Food(name,cost));
        }

        files.close();
        
    }


    static void writeFoods(deque<Food> savedFoods)
    {
        ofstream files("foods.txt");
        string name;
        double cost;
 
        for ( Food food: savedFoods)
        {
            files << food.name <<" "<< food.cost << endl;
        }
    
        files.close();
        

    }

    //constructor
    Food(string name, double cost){
        this->name = name;
        this->cost = cost;
    }
    Food(){
        
    }
};


int main(int argc, char const *argv[])

{
    // deque<Food> foods;
    // string file_name = "foods.txt";


    // Food food;
    // food.name="cheese";
    // food.cost=22.53;

    // foods.push_back(food);
    
    
    // Food food2;
    // food2.name = "chocolate";
    // food2.cost = 85.69;
    // foods.push_back(food2);
    
    // ofstream file(file_name);

    // for (auto food : foods)
    // {
    //     file << food.name << " " << food.cost << endl;
    // }
    
 



    
    deque<Food> savedFoods;
    Food::readFoods(savedFoods);
    //Food::printFoods(savedFoods);

    int response = 0;
    while (response != 6 && response != 7)
    {
        cout << "Choose an option:\n";
        cout << "1. display foods\n";
        cout << "2. add food to the front\n";
        cout << "3. add food to the back\n";
        cout << "4. remove food from the front\n";
        cout << "5. remove food from the back\n";
        cout << "6. save and quit\n";
        cout << "7. quit without saving\n";
        cout << "Your response: ";

        cin >> response;

        cout << " \n";
        string name;
        double cost;
        switch (response)
        {
        case 1:
            Food::printFoods(savedFoods);
            break;
        case 2:
            cout << "Food and cost? example: berry 5.25"<<endl;
            cin >> name>>cost;
            savedFoods.push_front(Food(name,cost));
            break;
        case 3:
            cout << "Food and cost? example: berry 5.25"<<endl;
            cin >> name>>cost;
            savedFoods.push_back(Food(name,cost));
            break;
        case 4:
            cout << "removing " << savedFoods.front().name << "...\n";
            savedFoods.pop_front();
            break;
        case 5:
            cout << "removing " << savedFoods.back().name << "...\n";
            savedFoods.pop_back();
            break;
        case 6:
            Food::writeFoods(savedFoods);
            break;
        case 7:
            break;
        
        default:
            break;
        }

        cout << endl;

    }
    

    system("pause");

    return 0;
}
