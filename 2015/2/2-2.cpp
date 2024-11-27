#include <bits/stdc++.h>
using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(false);

    int ans = 0;
    string s;
    while (cin >> s) {
        vector<int> lwh;  
        int start = 0, end;
        while ((end = s.find('x', start)) != string::npos) {
            lwh.push_back(stoi(s.substr(start, end - start)));
            start = end + 1;
        }
        lwh.push_back(stoi(s.substr(start, s.size())));
        int l = lwh[0], w = lwh[1], h = lwh[2];
        sort(lwh.begin(), lwh.end());
        ans += 2 * lwh[0] + 2 * lwh[1] + l * w * h;
    } 
    cout << ans;

    return 0;
}