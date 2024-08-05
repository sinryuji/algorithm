#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(vector<int> v) {
    return v.size() >= 11 ? accumulate(v.begin(), v.end(), 0) : accumulate(v.begin(), v.end(), 1, multiplies<int>());
}