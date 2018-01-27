#include<iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  bool arr[4][14];
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 14; j++){
      arr[i][j] = 0;
    }
  }
  
  char c;
  int a, b;
  for (int i = 0; i < n; i++) {
    cin >> c >> b;

    if (c == 'S') a = 0;
    if (c == 'H') a = 1;
    if (c == 'C') a = 2;
    if (c == 'D') a = 3;

    arr[a][b] = 1;
  }

  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 14; j++) {
      if (arr[i][j] == 0) {
	if (j == 0) continue;
	else {
	  if (i == 0) c = 'S';
	  if (i == 1) c = 'H';
	  if (i == 2) c = 'C';
	  if (i == 3) c = 'D';
	cout << c << " " << j << endl;
	}
      }
    }
  }
  return 0;
}
