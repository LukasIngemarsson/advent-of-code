#include <bits/stdc++.h>
using namespace std;

pair<int, int> dirs[] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
vector<string> grid;
int rows, cols;

set<pair<int, int>> obstructs;
set<tuple<int, int, int>> glob_visited, loc_visited;

bool in_visited(tuple<int, int, int> t) {
    return glob_visited.find(t) != glob_visited.end() || loc_visited.find(t) != loc_visited.end();
}

bool tile_visited(int r, int c) {
    for (int i = 0; i < 4; ++i) {
        if (glob_visited.find({r, c, i}) != glob_visited.end()) {
            return true;
        }
    }
    return false;
}

int get_next_dir(int idx) {
    return (idx + 1) % 4;
}

bool search(pair<int, int> pos, int dir_idx=0, bool global=true) {
    while (true) {
        if (global) {
            glob_visited.insert({pos.first, pos.second, dir_idx});
        }
        else {
            if (in_visited({pos.first, pos.second, dir_idx})) {
                return true;
            }
            loc_visited.insert({pos.first, pos.second, dir_idx});
        }
        int r = pos.first + dirs[dir_idx].first;
        int c = pos.second + dirs[dir_idx].second;
        if (r < 0 || r >= rows || c < 0 || c >= cols) {
            return false;
        }
        if (grid[r][c] == '#') {
            dir_idx = get_next_dir(dir_idx);
            continue;
        }
        if (global && !tile_visited(r, c)) {
            grid[r][c] = '#';
            if (search(pos, get_next_dir(dir_idx), false)) {
                obstructs.insert({r, c});
            }
            grid[r][c] = '.';
            loc_visited.clear();
        }
        pos = {r, c};
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(false);

    string s;
    while (getline(cin, s)) {
        grid.push_back(s);
    } 
    rows = grid.size(), cols = grid.front().size();
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
    search(start_pos);
    if (obstructs.find(start_pos) != obstructs.end()) {
        obstructs.erase(start_pos);
    }
    cout << obstructs.size() << endl;
    
    return 0;
}