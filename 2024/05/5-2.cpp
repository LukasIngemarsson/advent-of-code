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
    auto update_comp = [&] (int a, int b) {
        if (rules[a].find(b) != rules[a].end()) {
            return true;
        }
        return false;
    };
    do {
        vector<int> update = split_to_ints(line, ',');
        vector<int> sorted_update(update);
        sort(sorted_update.begin(), sorted_update.end(), update_comp);
        if (update != sorted_update) {
            ans += sorted_update[sorted_update.size() / 2];
        }
    } while (cin >> line);
    cout << ans;

    return 0;
}