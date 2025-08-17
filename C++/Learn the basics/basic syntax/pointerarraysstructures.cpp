#include <iostream>
using namespace std;

//pointers
char c = 'a';
char* p = &c;
int* pi; // pointer to int 
char** ppc; //pointer to pointer to char 
int* ap[15]; // aray of 15 pointers to ints
int (*fp) (char*); //pointer to function taking a char
//int* f(char*); // function taking char* argument; returns a pointer to int

//arrays
float v[3]; // an array of three floats: v[0],v[1],v[2]
char* a[32]; // an array of 32 pointers to char: a[0]....a[3]
int d2[10][20]; //d2 is a 2 dimension array 10 arrays of 20 integers



//initializing array
int v1[] = {1,2,3,4};// number of elements is the size of the array  else v1[3]  has to have 3  elements in it
char v2[] = {'a','b','c',0};

int main(int argc, char const *argv[])
{
    
    cout << v1[2] << endl;
    return 0;
}
