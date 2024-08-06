#include <iostream>

using namespace std;

int main(void) {
    string str;
    int zero = 0, one = 0, idx = 0;
    cin >> str;
    
    while (idx < str.length()) {
        char target = str[idx];
        if (target == '0') zero++;
        else one++;
        while (str[idx] == target) idx++;
    }
    
    cout << min(zero, one) << endl;
        
    return 0;
}