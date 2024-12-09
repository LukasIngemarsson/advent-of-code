#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    string file((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());   
    vector<int> v;
    int id_cnt{};
    for (int i = 0; i < file.size(); ++i) {
        for (int _ = 0; _ < file[i] - '0'; ++_) {
            v.push_back((i % 2 == 0) ? id_cnt : -1);
        }
        if (i % 2 == 0) {
            ++id_cnt;   
        }
    }
    int curr = -1;
    int w = 1;
    for (int i = v.size() - 1; i >= 0; --i) {
        if (curr == v[i]) {
            ++w;
        }
        else {
            if (curr != -1) {
                int free_cnt{};
                for (int j = 0; j <= i; ++j) {
                    if (v[j] == -1) {
                        if (++free_cnt >= w) {
                            for (int k = 0; k < w; ++k) {
                                v[j-k] = v[i+1+k];
                                v[i+1+k] = -1;
                            }
                            break;
                        }
                    }
                    else {
                        free_cnt = 0;
                    }
                }
            }
            w = 1;
            curr = v[i];
        }
    }
    long long ans{};
    for (int i = 0; i < v.size(); ++i) {
        if (v[i] == -1) {
            continue;
        }
        ans += i * v[i];
    }
    cout << ans << endl;

    return 0;
}