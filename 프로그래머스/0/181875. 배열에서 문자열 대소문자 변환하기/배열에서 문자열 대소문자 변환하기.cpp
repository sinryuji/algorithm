#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> strArr) {
    for (int i = 0; i < strArr.size(); ++i) {
        if (i & 1) transform(strArr[i].begin(), strArr[i].end(), strArr[i].begin(), ::toupper);
        else transform(strArr[i].begin(), strArr[i].end(), strArr[i].begin(), ::tolower);
    }
    return strArr;
}