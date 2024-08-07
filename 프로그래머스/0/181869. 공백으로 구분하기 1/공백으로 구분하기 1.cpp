#include <string>
#include <vector>

using namespace std;

vector<string> solution(string my_string) {
    vector<string> answer;
    
    string str = "";
    for (const char& c : my_string) {
        if (c == ' ') {
            answer.push_back(str);
            str = "";
        } else str.push_back(c);
    }
    answer.push_back(str);
    
    return answer;
}