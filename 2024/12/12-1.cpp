#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    vector<string> grid;
    string s;
    while (cin >> s) {
        grid.push_back(s);
    }
    int rows = grid.size(), cols = grid.front().size();
    set<pair<int, int>> visited;
    pair<int, int> dirs[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    auto bfs = [&] (int sr, int sc) -> int {
        char& ptype = grid[sr][sc];
        queue<pair<int, int>> q;
        q.push({sr, sc});
        visited.insert({sr, sc});

        int area{}, perim{};
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            ++area;
            for (auto& [dr, dc] : dirs) {
                int nr = r + dr, nc = c + dc;
                if (!(nr >= 0 && nr < rows && nc >= 0 && nc < cols) || grid[nr][nc] != ptype) {
                    ++perim;
                }
                else if (visited.find({nr, nc}) == visited.end()) {
                    q.push({nr, nc});
                    visited.insert({nr, nc});
                }
            }
        }
        return area * perim; 
    };

    int ans{};
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (visited.find({r, c}) == visited.end()) {
                ans += bfs(r, c);
            }
        }
    } 
    cout << ans << endl;

    return 0;
}