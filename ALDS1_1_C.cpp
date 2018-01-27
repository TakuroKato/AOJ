#include<iostream>
#include<cmath>
using namespace std;

bool isPrime(int a) {
  for (int i = 2; i <= sqrt(a); i++) {
    if (a % i == 0) {
      return false;
    }
  }

    return true;
}

int main() {

  int n;
  cin >> n;

  int sum = 0;
  int x;
  for (int i = 0; i < n; i++) {
    cin >> x;
    if (isPrime(x)) sum += 1; 
  }

  cout << sum << endl;
  
  return 0;
}
