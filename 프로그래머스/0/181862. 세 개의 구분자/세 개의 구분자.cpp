#include <string>
#include <vector>

using namespace std;

vector<string> solution(string myStr) {
    vector<string> answer;
    string tmp = "";
    
    for (const char& c: myStr) {
        if (c != 'a' && c != 'b' && c != 'c')
            tmp.push_back(c);
        else {
            if (tmp != "")
                answer.push_back(tmp);
            tmp = "";
        }
    }
    if (tmp != "")
        answer.push_back(tmp);
    if (answer.size() == 0)
        answer.push_back("EMPTY");
    
    return answer;
}