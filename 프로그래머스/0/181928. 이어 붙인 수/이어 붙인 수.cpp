#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    string odd = "";
    string even = "";
    
    for (int num : num_list) {
        if (num % 2 == 0) even.push_back(num + '0');
        else odd.push_back(num + '0');
    }
    
    return stoi(odd) + stoi(even);
}