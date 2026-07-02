class Solution {
public:
    static constexpr int dirs[4][2] = {
        {1,0},
        {0,1},
        {-1,0},
        {0,-1}
    };

    bool findSafeWalk(vector<vector<int>>& grid, int health) {

        int r = grid.size();
        int c = grid[0].size();

        const int INF = 1e9;

        vector<vector<int>> dist(r, vector<int>(c, INF));

        deque<pair<int,int>> dq;

        dist[0][0] = grid[0][0];
        dq.push_front({0,0});

        while (!dq.empty()) {

            auto [y,x] = dq.front();
            dq.pop_front();

            for (auto &d : dirs) {

                int ny = y + d[1];
                int nx = x + d[0];

                if (ny < 0 || ny >= r || nx < 0 || nx >= c)
                    continue;

                int nd = dist[y][x] + grid[ny][nx];

                if (nd >= dist[ny][nx])
                    continue;

                dist[ny][nx] = nd;

                if (grid[ny][nx] == 0)
                    dq.push_front({ny,nx});
                else
                    dq.push_back({ny,nx});
            }
        }

        return dist[r-1][c-1] < health;
    }
};