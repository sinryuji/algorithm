#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    if (n == 1 || n == 3) {
        cout << -1 << endl;
        return 0;
    }
    int answer = n / 5;
    int remain = n % 5;
    if (remain & 1) {
        answer--;
        remain += 5;
    }
    answer += remain / 2;
    cout << answer << endl;
    return 0;
}