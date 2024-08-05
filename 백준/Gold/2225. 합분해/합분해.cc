#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int N, K;
    cin >> N >> K;
    vector<vector<int> > dp(N+1, vector<int>(K+1, 0));
    
    for (int i = 0; i <= K; i++)
        dp[1][i] = i;
    
    for (int i = 2; i <= N; i++)
        for (int j = 1; j <= K; j++)
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000;
            
    cout << dp[N][K] << endl;
    
    return 0;
}
