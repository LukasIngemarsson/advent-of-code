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
    vector<string> grid = split(file, "\n");
    int rows = grid.size(), cols = grid.front().size();

    unordered_map<char, vector<pair<int, int>>> ant_locs;
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] == '.') {
                continue;
            }
            ant_locs[grid[r][c]].push_back({r, c});
        }
    }
    set<pair<int, int>> antidotes;
    for (auto& [_, locs] : ant_locs) {
        sort(locs.begin(), locs.end());
        for (int i = 0; i < locs.size(); ++i) {
            int ir = locs[i].first, ic = locs[i].second;
            for (int j = i + 1; j < locs.size(); ++j) {
                int jr = locs[j].first, jc = locs[j].second;
                int diffr = jr - ir;
                int diffc = jc - ic;
                int roff{}, coff{};
                while (ir - roff >= 0 && ir - roff < rows && ic - coff >= 0 && ic - coff < cols) {
                    antidotes.insert({ir - roff, ic - coff});
                    roff += diffr;
                    coff += diffc;
                }
                roff = 0, coff = 0;
                while (jr + roff >= 0 && jr + roff < rows && jc + coff >= 0 && jc + coff < cols) {
                    antidotes.insert({jr + roff, jc + coff});
                    roff += diffr;
                    coff += diffc;
                }
            }
        }
    }
    cout << antidotes.size() << endl;

    return 0;
}