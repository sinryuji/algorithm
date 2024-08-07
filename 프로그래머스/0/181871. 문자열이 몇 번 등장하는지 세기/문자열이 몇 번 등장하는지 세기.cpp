#include <string>
#include <vector>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    
    size_t pos = 0;
    while ((pos = myString.find(pat, pos)) != string::npos) {
        pos++;
        answer++;
    }
    
    return answer;
}