#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(false);

    string file((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());   
    regex int_regex(R"(\d+)");
    vector<int> nums;
    smatch match;
    string::const_iterator start(file.cbegin());
    while (regex_search(start, file.cend(), match, int_regex)) {
        nums.push_back(stoi(match.str()));
        start = match.suffix().first;
    }
    long long ans{};
    for (int i = 0; i < nums.size(); i += 6) {
        int ax = nums[i], ay = nums[i+1];
        int bx = nums[i+2], by = nums[i+3];
        int tx = nums[i+4], ty = nums[i+5];
        int min_cost = INT_MAX;
        for (int a = 1; a <= 100; ++a) {
            for (int b = 1; b <= 100; ++b) {
                if (a * ax + b * bx > tx || a * ay + b * by > ty) {
                    break;
                }
                if (a * ax + b * bx == tx && a * ay + b * by == ty) {
                    min_cost = min(min_cost, 3 * a + b);
                    break;
                }
            }
        }
        ans += (min_cost < INT_MAX) ? min_cost : 0;
    }
    cout << ans << endl;

    return 0;
}