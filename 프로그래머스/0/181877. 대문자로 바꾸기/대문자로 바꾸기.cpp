#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    for (char& c : myString) c = toupper(c);
    return myString;
}