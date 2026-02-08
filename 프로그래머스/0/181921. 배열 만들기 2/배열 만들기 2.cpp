#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int l, int r) {
    vector<int> answer;
    
    for (int i = l; i <= r; i++) {
        string str = to_string(i);
        bool flag = true;
        for (char c : str) {
            if (c != '0' && c != '5') flag = false;
        }
        if (flag) answer.push_back(i);
    }
    
    if (answer.size() == 0) answer.push_back(-1);
    
    return answer;
}