#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer;
    bool check[100001] = {false};
    
    for (int i = 0; i < arr.size() && k > 0; i++) {
        if (check[arr[i]])
            continue;
        answer.push_back(arr[i]);
        check[arr[i]] = true;
        k--;
    }
    
    while (k--)
        answer.push_back(-1);
    
    return answer;
}