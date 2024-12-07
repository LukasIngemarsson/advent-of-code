#include <bits/stdc++.h>
using namespace std;

pair<int, int> dirs[] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
vector<string> grid;
int rows, cols;

set<pair<int, int>> obstructs;
set<tuple<int, int, int>> glob_visited;
set<tuple<int, int, int>> loc_visited;

bool in_visited(tuple<int, int, int> t) {
    return glob_visited.find(t) != glob_visited.end() || loc_visited.find(t) != loc_visited.end();
}

int get_next_idx(int idx) {
    return (idx + 1) % 4;
}

bool search(pair<int, int> pos, int dir_idx=0, bool check_obstructs=true) {
    while (true) {
        if (check_obstructs) {
            glob_visited.insert({pos.first, pos.second, dir_idx});
        }
        else {
            loc_visited.insert({pos.first, pos.second, dir_idx});
        }
        int r = pos.first + dirs[dir_idx].first;
        int c = pos.second + dirs[dir_idx].second;
        if (r < 0 || r >= rows || c < 0 || c >= cols) {
            return false;
        }
        if (grid[r][c] == '#') {
            dir_idx = get_next_idx(dir_idx);
            continue;
        }
        if (check_obstructs) {
            grid[r][c] = '#';
            if (search(pos, get_next_idx(dir_idx), false)) {
                obstructs.insert({r, c});
            }
            grid[r][c] = '.';
            loc_visited.clear();
        }
        else if (in_visited({r, c, dir_idx})) {
            return true;
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

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (make_pair(r, c) == start_pos) {
                cout << 'S';
            }
            // else if (glob_visited.find({r, c}) != glob_visited.end()) {
            //     cout << 'X';
            // }
            else if (obstructs.find({r, c}) != obstructs.end()) {
                cout << '0';
            }
            else {
                cout << grid[r][c];
            }
        }
        cout << endl;
    }
    
    return 0;
}