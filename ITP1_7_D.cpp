#include<iostream>
using namespace std;

int main() {
  int n, m, l;
  cin >> n >> m >> l;

  int A[n][m], B[m][l];
  
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> A[i][j];
    }
  }

  for (int i = 0; i < m; i++) {
    for (int j = 0; j < l; j++) {
      cin >> B[i][j];
    }
  }

  
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < l; j++){
      long long  c = 0;
      for (int k = 0; k < m; k++) {
	c += A[i][k]*B[k][j];
      }
      cout << c;
      if (j < l-1) cout << " ";
    }
    cout << endl;
  }
    
  return 0;
}
