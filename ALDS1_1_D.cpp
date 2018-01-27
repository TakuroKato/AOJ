#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
static const int MAX = 200000;

int main() {

  int r[MAX], n;

  cin >> n;
  for (int i = 0; i < n; i++) cin >> r[i];

  int maxv = -1000000000;
  int minv = r[0];

  for (int i = 1; i < n; i++) {
    maxv = max(maxv,r[i] - minv);
    minv = min(minv,r[i]);    
  }

  cout << maxv << endl;
  
  return 0;
}
