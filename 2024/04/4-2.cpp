#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    string line;
    vector<string> grid;
    while (getline(cin, line)) {
        grid.push_back(line);
    }
    int rows = grid.size(), cols = grid[0].size();
    int ans{};
    pair<int, int> dirs[] = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            int cnt{};
            for (auto& [dr, dc] : dirs) {
                string s;
                int newr{}, newc{};
                for (int i = 0; i < 3; ++i) { 
                    newr = (r + dr) - i * dr;
                    newc = (c + dc) - i * dc;
                    if (newr < 0 || newr >= rows || newc < 0 || newc >= cols) {
                        break;
                    }
                    s.push_back(grid[newr][newc]);
                }
                if (s == "MAS" && ++cnt > 1) {
                    ++ans;
                    break;
                }
            }
        }
    }
    cout << ans;

    return 0;
}