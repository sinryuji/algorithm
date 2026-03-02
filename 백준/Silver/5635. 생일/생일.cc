#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int main() {
    int n;
    vector<tuple<int, int, int, string>> v;
    
    cin >> n;
    
    string name;
    int d, m, y;
    while (cin >> name >> d >> m >> y)
        v.emplace_back(y, m, d, name);
    
    sort(v.begin(), v.end());
    
    cout << get<3>(v[n-1]) << endl;
    cout << get<3>(v[0]) << endl;
}