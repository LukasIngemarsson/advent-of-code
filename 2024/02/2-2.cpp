#include <bits/stdc++.h>
using namespace std;

vector<string> split(string s, char delim) {
    vector<string> v;  
    int start = 0, end;
    while ((end = s.find(delim, start)) != string::npos) {
        v.push_back(s.substr(start, end - start));
        start = end + 1;
    }
    v.push_back(s.substr(start, s.size()));
    return v;
}

string strip(string s) {
    int start = s.find_first_not_of(" \t\n\r\f\v");
    int end = s.find_last_not_of(" \t\n\r\f\v");
    return (start == string::npos) ? "" : s.substr(start, end + 1);
}

bool is_safe(vector<string>& split_s) {
    for (int k = 0; k < split_s.size(); ++k) {
        vector<string> temp = split_s;
        temp.erase(temp.begin() + k);

        int valid = true;
        bool increasing = true;
        for (int i = 0; i < temp.size() - 1; ++i) {
            int diff = stoi(temp[i]) - stoi(temp[i+1]);
            if (diff <= -1 && diff >= -3) {
                if (i > 0 && !increasing) {
                    valid = false;
                    break;
                }
            }
            else if (diff >= 1 && diff <= 3) {
                if (i == 0) {
                    increasing = false;
                }
                else if (increasing) {
                    valid = false;
                    break;
                }
            }
            else {
                valid = false;
                break;
            }
        }
        if (valid) {
            return true;
        }
    }
    return false;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);

    string s;
    int ans = 0;
    while (getline(cin, s)) {
        vector<string> split_s = split(strip(s), ' ');
        if (is_safe(split_s)) {
            ++ans;
        }
    }
    cout << ans;
    
    return 0;
}