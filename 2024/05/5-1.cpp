#include <bits/stdc++.h>
using namespace std;

vector<int> split_to_ints(string s, char delim=' ') {
    vector<int> v;
    int start = 0, end;
    while ((end = s.find(delim, start)) != string::npos) {
        v.push_back(stoi(s.substr(start, end - start)));
        start = end + 1;
    }
    v.push_back(stoi(s.substr(start, s.size())));
    return v;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);

    string line;
    unordered_map<int, unordered_set<int>> rules;
    while (cin >> line) {
        vector<int> rule = split_to_ints(line, '|');
        if (rule.size() < 2) {
            break;
        }
        rules[rule[0]].insert(rule[1]);       
    } 
    int ans{};
    do {
        vector<int> update = split_to_ints(line, ',');
        int update_len = update.size();
        for (int i = 0; i < update_len; ++i) {
            int ival = update[i];
            for (int j = i + 1; j < update_len; ++j) {
                int jval = update[j];
                if (rules[jval].find(ival) != rules[jval].end()) {
                    goto out_label;
                }
            }
        }
        ans += update[update_len / 2];
        out_label:;
    } while (cin >> line);
    cout << ans;

    return 0;
}