#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    std::string file((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    std::regex mul_format(R"(mul\((\d+),(\d+)\))");

    auto start = std::sregex_iterator(file.begin(), file.end(), mul_format);
    auto end = std::sregex_iterator();

    int ans{}, a, b;
    for (auto it = start; it != end; ++it) {
        a = stoi((*it)[1]), b = stoi((*it)[2]);
        ans += a * b;
    }
    cout << ans;
    
    return 0;
}