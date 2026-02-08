#include <string>
#include <vector>
#include <numeric>
#include <cmath>

#define all(x) x.begin(), x.end()

using namespace std;

int solution(vector<int> num_list) {
    return accumulate(all(num_list), 1, multiplies<int>()) < pow(accumulate(all(num_list), 0), 2);
}