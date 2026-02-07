#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int k = (n + 1) >> 1;
    
    return n & 1 ? k * k : (2 * k) * (k + 1) * (2 * k + 1) / 3;
}