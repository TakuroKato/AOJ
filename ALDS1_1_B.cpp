#include<iostream>
#include<cmath>
using namespace std;

int gcd(int a, int b) {
  int tmp;
  if (a < b) {
    tmp = b;
    b = a;
    a = tmp;
  }

  int c;
  
  while (b != 0) {
    c = a % b;
    a = b;
    b = c;
  }

  return a;
  
}

int main() {

  int x, y;
  cin >> x >> y;

  cout << gcd(x, y) << endl;
  
  return 0;
}
