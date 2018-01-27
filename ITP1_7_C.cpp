#include<iostream>
using namespace std;

int main() {
  int r, c;
  cin >> r >> c;

  int arr[r][c];
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      cin >> arr[i][j];
    }
  }

  for (int i = 0; i < r; i++) {
    int sum_r = 0;
    for (int j = 0; j < c; j++) {
      cout << arr[i][j] << " ";
      sum_r += arr[i][j];
    }
    cout << sum_r << endl;
  }

  int total = 0;
    
  for (int i = 0; i < c; i++) {
    int sum_c = 0;
    for (int j = 0; j < r; j++) {
      sum_c += arr[j][i];
    }
    cout << sum_c << " ";
    total += sum_c;
  }

  cout << total << endl;

  return 0;
}
