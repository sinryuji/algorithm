#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int N;
    string line;
    vector<string> board;
    
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> line;
        board.push_back(line);
    }
    
    int rowCnt = 0, colCnt = 0;
    for (int i = 0; i < N; ++i) {
        int rCnt = 0, cCnt = 0;
        bool rFlag = true, cFlag = true;
        for (int j = 0; j < N; ++j) {
            if (board[i][j] == '.') ++rCnt;
            else {
              rCnt = 0;
              rFlag = true;
            }
            if (board[j][i] == '.') ++cCnt;
            else {
              cCnt = 0;
              cFlag = true;
            }
            if (rCnt >= 2 && rFlag) {
              ++rowCnt;
              rFlag = false;
            }
            if (cCnt >= 2 && cFlag) {
              ++colCnt;
              cFlag = false;
            }
        }
    }
    
    cout << rowCnt << ' ' << colCnt;

    return 0;
}
