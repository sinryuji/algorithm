#include <iostream>

using namespace std;

int main(void) {
    string a, b;
    getline(cin, a);
    getline(cin, b);
    
    int pos = 0, ans = 0;
    while ((pos = a.find(b, pos)) != string::npos) {
        pos += b.length();
        ans++;
    }

    cout << ans << endl;

    return 0;
}