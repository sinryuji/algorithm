#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    string str_a = to_string(a);
    string str_b = to_string(b);
    
    int ab = stoi(str_a + str_b);
    int ba = stoi(str_b + str_a);
    
    return ba > ab ? ba : ab;
}