#include<iostream>
using namespace std;

int main(){
  int a, b, tmp;

  for(;;){
    cin >> a >> b;
    if (a == 0 && b == 0) break;
    if ( a > b) {
      tmp = a;
      a = b;
      b = tmp;
      cout << a << " " << b << endl;
    } else {
      cout << a << " " << b << endl;
    }
  }

  return 0;
}
