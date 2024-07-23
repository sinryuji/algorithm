#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer;
    
    for (auto q : queries) {
        vector<int> tmp;
        for (int i = q[0]; i <= q[1]; i++)
            if (arr[i] > q[2]) tmp.push_back(arr[i]);
        answer.push_back(tmp.size() > 0 ? *min_element(tmp.begin(), tmp.end()) : -1);
    }
    
    return answer;
}