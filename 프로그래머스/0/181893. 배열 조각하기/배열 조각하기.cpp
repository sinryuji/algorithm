#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr, vector<int> query) {
    for (int i = 0; i < query.size(); i++) {
        if (i & 1) arr = vector<int>(arr.begin() + query[i], arr.end());
        else arr = vector<int>(arr.begin(), arr.begin() + query[i] + 1);
        cout << arr.size() << endl;
        
    }
    return arr;
}