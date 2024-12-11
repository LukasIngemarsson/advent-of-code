#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    vector<string> stones;
    string s;
    while (cin >> s) {
        stones.push_back(s);
    }
    for (int i = 0; i < 25; ++i) {
        int init_size = stones.size();
        for (int j = 0; j < init_size; ++j) {
            string& s = stones[j];
            if (s == "0") {
                s = "1";
            }
            else if (s.size() % 2 == 0) {
                string left = s.substr(s.size() / 2, s.size());
                string right = s.substr(0, s.size() / 2);
                s = to_string(stoll(left));
                stones.push_back(to_string(stoll(right)));
            }
            else {
                s = to_string(stoll(s) * 2024);
            }
        }
    }
    cout << stones.size() << endl;

    return 0;
}