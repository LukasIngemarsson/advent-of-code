#include <bits/stdc++.h>
using namespace std;

vector<string> split(string s, char delim=' ') {
    vector<string> v;  
    int start = 0, end;
    while ((end = s.find(delim, start)) != string::npos) {
        v.push_back(s.substr(start, end - start));
        start = end + 1;
    }
    v.push_back(s.substr(start, s.size()));
    return v;
}

long long ans{};
long long test_val;
vector<long long> nums;
bool valid = false;

void dfs(int idx=0, long long sum=0) {
    if (valid) {
        return;
    }
    if (idx >= nums.size()) {
        if (sum == test_val) {
            ans += test_val;
            valid = true;
        }
        return;
    }
    dfs(idx + 1, sum * nums[idx]);
    dfs(idx + 1, sum + nums[idx]);
}

void reset_glob() {
    valid = false;
    nums.clear();
}

int main() {
    cin.tie(0)->sync_with_stdio(false);

    string line;
    while (getline(cin, line)) {
        vector<string> split_line = split(line);
        test_val = stoll(split_line[0].substr(0, split_line[0].size() - 1));
        split_line.erase(split_line.begin());
        for (string s : split_line) {
            nums.push_back(stoll(s));
        }
        dfs();
        reset_glob();
    }
    cout << ans << endl;

    return 0;
}