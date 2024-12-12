#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    vector<string> stones;
    string s;
    while (cin >> s) {
        stones.push_back(s);
    }

    map<pair<string, int>, long long> state;
    auto dfs = [&] (auto&& dfs, string s, int iter) -> long long {
        if (iter == 0) {
            return 1;
        }
        if (state.find({s, iter}) == state.end()) {
            long long res{};
            if (s == "0") {
                res += dfs(dfs, "1", iter - 1);
            }
            else if (s.size() % 2 == 0) {
                string left = s.substr(s.size() / 2, s.size());
                string right = s.substr(0, s.size() / 2);
                res += dfs(dfs, to_string(stoll(left)), iter - 1);
                res += dfs(dfs, to_string(stoll(right)), iter - 1);
            }
            else {
                res += dfs(dfs, to_string(stoll(s) * 2024), iter - 1);
            }
            state[{s, iter}] = res;
        }
        return state[{s, iter}];
    };

    long long ans{};
    for (string s : stones) {
        ans += dfs(dfs, s, 75);
    }
    cout << ans << endl;

    return 0;
}