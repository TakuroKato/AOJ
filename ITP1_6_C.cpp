#include<iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  int arr[5][4][11];
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 11; k++) {
	arr[i][j][k] = 0;
      }
    }
  }
  
  int b, f, r, v;
  for (int i = 0; i < n; i++) {
    cin >> b >> f >> r >> v;
    arr[b][f][r] += v;
  }

  for (int i = 1; i < 5; i++) {
    for (int j = 1; j < 4; j++) {
      for (int k = 1; k < 11; k++) {
	cout << " "  << arr[i][j][k];
      }
      cout << endl;
    }
    if (i != 4) cout << "####################" << endl;
  }
  
  return 0;
}
