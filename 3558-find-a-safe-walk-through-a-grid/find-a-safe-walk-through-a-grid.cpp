class Solution {
public:
    static constexpr int dirs[4][2] = {{1, 0}, {0, 1}, {-1, 0},{0, -1}};

    bool findSafeWalk(vector<vector<int>>& grid, int health) {

        int r = grid.size();
        int c = grid[0].size();

        vector<vector<int>> best(r, vector<int>(c, -1));

        queue<tuple<int,int,int>> q;

        if (grid[0][0])
            health--;

        q.push({0,0,health});

        while (!q.empty()) {

            auto [x,y,h] = q.front();
            q.pop();

            if (h <= 0)
                continue;

            if (best[y][x] >= h)
                continue;

            best[y][x] = h;

            if (y == r-1 && x == c-1)
                return true;

            for (auto &d : dirs) {

                int nx = x + d[0];
                int ny = y + d[1];

                if (0 <= nx && nx < c &&
                    0 <= ny && ny < r) {

                    if (grid[ny][nx])
                        q.push({nx, ny, h-1});
                    else
                        q.push({nx, ny, h});
                }
            }
        }

        return false;
    }
};