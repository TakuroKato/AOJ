#include<cstdio>

int main() {
  int a, b;
  scanf("%d %d", &a, &b);
  printf("%d %d %.7f\n", a / b, a % b, (double) a / (double) b);
  return 0;
}
