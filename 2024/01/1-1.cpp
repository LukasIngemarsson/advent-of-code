#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    vector<int> v1, v2; 
    int a, b;
    while (cin >> a >> b) {
        v1.push_back(a);
        v2.push_back(b);
    }
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    int ans = 0;
    for (int i = 0; i < v1.size(); ++i) {
        ans += abs(v1[i] - v2[i]);
    }
    cout << ans;

    return 0;
}