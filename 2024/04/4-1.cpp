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
    pair<int, int> dirs[] = {{0, 1}, {1, 1}, {1, 0}, {1, -1}, 
                            {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}};
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            for (auto& [dr, dc] : dirs) {
                string s;
                for (int i = 0; i < 4; ++i) {
                    int newr = r + i * dr, newc = c + i * dc;
                    if (newr < 0 || newr >= rows || newc < 0 || newc >= cols) {
                        break;
                    }
                    s.push_back(grid[newr][newc]);
                }
                if (s == "XMAS") {
                    ++ans;
                }
            }
        }
    }
    cout << ans;

    return 0;
}