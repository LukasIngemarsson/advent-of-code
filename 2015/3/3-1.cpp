#include <bits/stdc++.h>
using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(false);

    char ch;
    set<pair<int, int>> visited;
    pair<int, int> pos = {0, 0};
    while (cin >> ch) {
        switch (ch) {
            case '^':
                ++pos.second;
                break;
            case '>':
                ++pos.first;
                break;
            case 'v':
                --pos.second;
                break;
            case '<':
                --pos.first;
                break;
        }
        visited.insert(pos);
    }
    cout << visited.size();

    return 0;
}