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
    bool increasing = true;
    for (int i = 0; i < split_s.size() - 1; ++i) {
        int diff = stoi(split_s[i]) - stoi(split_s[i+1]);
        if (diff <= -1 && diff >= -3) {
            if (i > 0 && !increasing) {
                return false;
            }
        }
        else if (diff >= 1 && diff <= 3) {
            if (i == 0) {
                increasing = false;
            }
            else if (increasing) {
                return false;
            }
        }
        else {
            return false;
        }
    }
    return true;
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