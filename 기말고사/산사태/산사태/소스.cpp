#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<int> limit(n - 1);
    for (int& i : limit) cin >> i;
    limit.push_back(2e9);

    vector<vector<pair<int, int>>> data(n); // {key, size}
    auto push_back = [&](int level, int k, int size) {
        for (int i = 0; i < data[level].size(); i++) {
            if (data[level][i].first == k) {
                data[level].erase(data[level].begin() + i);
                break;
            }
        }

        data[level].emplace_back(k, size);
    };
    function<void(int)> update = [&](int level) {
        int sum = 0;
        for (const auto& [k, sz] : data[level]) {
            sum += sz;
        }

        if (sum > limit[level]) {
            for (const auto& [k, sz] : data[level]) push_back(level + 1, k, sz);
            data[level].clear();
            update(level + 1);
        }
    };

    while (q--) {
        char operat;
        cin >> operat;

        if (operat == 'I') {
            int k, S;
            cin >> k >> S;

            push_back(0, k, S);
            update(0);
        }
        else {
            int k;
            cin >> k;

            pair<int, int> answer = { -1, -1 };
            for (int i = 0; i < n && answer.second == -1; i++) {
                for (const auto& [kk, sz] : data[i]) {
                    if (kk == k) {
                        answer = { i + 1, sz };
                        break;
                    }
                }
            }

            if (answer.second == -1) cout << "none\n";
            else cout << answer.first << " " << answer.second << "\n";
        }
    }
}