#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    if (n & 1)
        answer = pow((n + 1) / 2, 2);
    else {
        int k = n / 2;
        answer = (2 * k) * (k + 1) * (2 * k + 1) / 3;
    }        
    
    return answer;
}