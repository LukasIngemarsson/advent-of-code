#include <bits/stdc++.h>
using namespace std;

int main() {
    std::cin.tie(0)->sync_with_stdio(false);

    char ch;
    set<pair<int, int>> visited;
    pair<int, int> pos = {0, 0};
    pair<int, int> robo_pos = {0, 0};
    auto update = [&visited](char ch, pair<int, int>& p) {
        switch (ch) {
            case '^':
                ++p.second;
                break;
            case '>':
                ++p.first;
                break;
            case 'v':
                --p.second;
                break;
            case '<':
                --p.first;
                break;
        }
        visited.insert(p);
    };
    bool is_robo = false;
    while (cin >> ch) {
        if (is_robo) update(ch, robo_pos);
        else update(ch, pos);
        is_robo = !is_robo;
    }
    cout << visited.size();
    
    return 0;
}