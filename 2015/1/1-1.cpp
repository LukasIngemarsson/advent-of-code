#include <bits/stdc++.h>
using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(false);

    string s;
    cin >> s;
    int ans = 0;
    for (char ch : s) {
        if (ch == '(') ++ans;
        else --ans;
    }    
    cout << ans;

    return 0;
}