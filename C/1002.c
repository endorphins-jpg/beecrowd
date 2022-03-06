#include <stdio.h>

#define P  3.14159

int main(void) {
  double raio, a;
  
  scanf("%lf", &raio);
  
  a = P  * (raio * raio);

  printf("A=%.4lf\n", a);
  return 0;
}