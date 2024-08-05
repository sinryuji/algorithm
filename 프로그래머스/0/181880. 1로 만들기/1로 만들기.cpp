#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    
    for (int& num : num_list) {
        while (num > 1) {
            if (num & 1) num = (num-1) / 2;
            else num /= 2;
            answer++;
        }
    }
    
    return answer;
}