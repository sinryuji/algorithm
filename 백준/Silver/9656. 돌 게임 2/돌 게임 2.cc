#include <ios>

int main(void) {
    int n;
    scanf("%d", &n);
    
    if (n & 1) printf("CY");
    else printf("SK");
}