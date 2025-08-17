/*

we are learning about declarations 
*/

#include <string>
using namespace std;


char ch;
string s;
int count =1;
const double pi = 3.145926535897932385;
extern int error_number;

const char* name = "james";
const char* season[]={"spring","summer","winter","fall"};

struct Date {int d,m,y;};
int day(Date*p) { return p->d;}
double sqrt(double);
template<class T> T abs(T a) { return a<0 ? -a:a;}

//typedef complex<short> Point;
struct User;
enum Beer {star,car,Thor};
namespace NS {int a;}


double sqrt(double d){

}

int error_number = 1;
struct User {

};