#include <bits/stdc++.h>
using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(false);

    string s;
    cin >> s;
    int ans = 0;
    for (int i = 0; i < s.size(); ++i) {
        char ch = s[i];
        if (ch == '(') ++ans;
        else --ans;
        if (ans == -1) {
            cout << i + 1;
            break;
        }
    }    

    return 0;
}