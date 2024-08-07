#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int N, M;
    cin >> N >> M;

    vector<vector<int>> painting(101, vector<int>(101, 0));
    int x1, y1, x2, y2;
    for (int i = 0; i < N; ++i) {
        cin >> x1 >> y1 >> x2 >> y2;
        
        for (int i = y1; i <= y2; ++i)
            for (int j = x1; j <= x2; ++j)
                ++painting[i][j];
    }
    
    int ans = 0;
    for (int i = 1; i <= 100; ++i)
        for (int j = 1; j <= 100; ++j)
            if (painting[i][j] > M) ++ans;
    
    cout << ans << endl;
    
    return 0;
}
