#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    vector<int> v1; 
    map<int, int> v2;
    int a, b;
    while (cin >> a >> b) {
        v1.push_back(a);
        ++v2[b];
    }
    int ans = 0;
    for (int i = 0; i < v1.size(); ++i) {
        ans += v1[i] * v2[v1[i]];
    }
    cout << ans;

    return 0;
}