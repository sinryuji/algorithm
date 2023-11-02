#include <iostream>
#include <vector>

int main() {
    int N;

    std::cin >> N;
    std::vector<int> v(N);

    for (int i = 0; i < N; i++) {
        std::cin >> v[i];
    }

    int target;
    std::cin >> target;
    int answer = 0;

    for (int i = 0; i < N; i++) {
        if (v[i] == target) {
            answer++;
        }
    }

    std::cout << answer;
}