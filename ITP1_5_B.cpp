#include<iostream>
using namespace std;

int rect(int h, int w){
  for (int k = 0; k < h; k++) {
    for (int i = 0; i < w; i++) {
      if (k == 0 or k == h-1 or i == 0 or i == w-1) cout << "#";
      else cout << ".";
    }
    cout << endl;
  }

  cout << endl;
  return 0;
}

int main() {
  int a, b;
  for (;;) {
    cin >> a >> b;
    if (a == 0 && b == 0) break;

    rect(a, b);
  }

  return 0;
}
