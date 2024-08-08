#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

vector<int> solution(string myString) {
    vector<int> answer;
    istringstream ss(myString);
    string tmp;
    
    while (getline(ss, tmp, 'x'))
        answer.push_back(tmp.length());
    
    if (myString[myString.length()-1] == 'x') answer.push_back(0);
    
    return answer;
}