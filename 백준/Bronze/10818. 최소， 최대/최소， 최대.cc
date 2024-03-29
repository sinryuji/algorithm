#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    int N;
    std::cin >> N;
    std::vector<int> v(N);

    for (int i = 0; i < N; i++) {
        std::cin >> v[i];
    }

    std::cout << *std::min_element(v.begin(), v.end());
    std::cout << " ";
    std::cout << *std::max_element(v.begin(), v.end());
 }