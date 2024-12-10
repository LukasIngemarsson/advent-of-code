#include <bits/stdc++.h>
using namespace std;

vector<string> split(string& s, string delim=" ") {
    vector<string> v;  
    int start = 0, end;
    while ((end = s.find(delim, start)) != string::npos) {
        v.push_back(s.substr(start, end - start));
        start = end + 1;
    }
    v.push_back(s.substr(start, s.size()));
    return v;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);

    string file((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());   
    vector<string> lines = split(file, "\n");
    vector<vector<int>> grid;
    for (string& l : lines) {
        grid.push_back({});
        for (char ch : l) {
            grid.back().push_back(ch - '0');
        }
    }
    int rows = grid.size(), cols = grid.front().size();
    pair<int, int> dirs[] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    auto bfs = [&] (int startr, int startc) -> int {
        queue<vector<pair<int, int>>> q;
        q.push({{startr, startc}});
        set<vector<pair<int, int>>> paths;

        while (!q.empty()) {
            vector<pair<int, int>> path = q.front();
            q.pop();
            pair<int, int> p = path.back();

            if (grid[p.first][p.second] == 9) {
                paths.insert(path);
                continue;
            }
            for (auto& d : dirs) {
                int nr = p.first + d.first;
                int nc = p.second + d.second;
                if (!(nr >= 0 && nr < rows && nc >= 0 && nc < cols)) {
                    continue;
                }
                if (grid[nr][nc] - grid[p.first][p.second] == 1) {
                    vector<pair<int, int>> npath(path);
                    npath.push_back({nr, nc});
                    q.push(npath);
                }
            }
        }
        return paths.size();
    };

    int ans{};
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] == 0) {
                ans += bfs(r, c);
            }
        }
    }
    cout << ans << endl;

    return 0;
}