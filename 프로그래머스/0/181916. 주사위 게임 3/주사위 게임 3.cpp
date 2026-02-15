#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int solution(int a, int b, int c, int d) {
    int answer = 0;
    
    vector<int> v(7, 0);
    v[a]++; v[b]++; v[c]++; v[d]++;
    vector<vector<int>> vv(5);
    for (int i = 0; i < v.size(); i++)
        vv[v[i]].push_back(i);
    
    if (vv[4].size() == 1)
        answer = 1111 * vv[4][0];
    else if (vv[3].size() == 1 && vv[1].size() == 1)
        answer = (10 * vv[3][0] + vv[1][0]) * (10 * vv[3][0] + vv[1][0]);
    else if (vv[2].size() == 2)
        answer = (vv[2][0] + vv[2][1]) * abs(vv[2][0] - vv[2][1]);
    else if (vv[2].size() == 1, vv[1].size() == 2)
        answer = vv[1][0] * vv[1][1];
    else
        answer = *min_element(vv[1].begin(), vv[1].end());
    
    return answer;
}