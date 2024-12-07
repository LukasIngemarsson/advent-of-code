#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    vector<string> grid;
    string s;
    while (getline(cin, s)) {
        grid.push_back(s);
    } 
    int rows = grid.size(), cols = grid.front().size();
    pair<int, int> start_pos;
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] == '^') {
                start_pos = {r, c};
                grid[r][c] = '.';
                goto out_label;
            }
        }
    }
    out_label:
    pair<int, int> dirs[] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    set<pair<int, int>> visited;
    pair<int, int> pos = start_pos;
    int dir_idx = 0;

    while (true) {
        visited.insert(pos);
        int r = pos.first + dirs[dir_idx].first;
        int c = pos.second + dirs[dir_idx].second;
        if (r < 0 || r >= rows || c < 0 || c >= cols) {
            break;
        }
        if (grid[r][c] == '#') {
            dir_idx = (dir_idx + 1) % 4; 
        }
        else {
            pos = {r, c};
        }
    }
    cout << visited.size() << endl;

    return 0;
}