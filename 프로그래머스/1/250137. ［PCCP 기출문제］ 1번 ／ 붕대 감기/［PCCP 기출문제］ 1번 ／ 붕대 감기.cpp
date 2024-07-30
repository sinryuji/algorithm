#include <string>
#include <vector>

using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int t = 0;
    int cur_health = health;
    auto cur_attack = attacks.begin();
    int conti = 0;
    while (true) {
        t += 1;
        if ((*cur_attack)[0] == t) {
            conti = 0;
            cur_health -= (*cur_attack)[1];
            if (cur_health <= 0) break;
            cur_attack = next(cur_attack);
            if (cur_attack == attacks.end()) break;
        } else {
            if (cur_health < health) {
            cur_health += bandage[1];
            conti++;
            if (conti == bandage[0]) {
                conti = 0;
                cur_health += bandage[2];
            }
            if (cur_health >= health) cur_health = health;
            }
        }

    }
    return cur_health <= 0 ? -1 : cur_health;
}