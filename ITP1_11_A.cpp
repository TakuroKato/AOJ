#include<iostream>
#include<cstdio>
using namespace std;

class Cube {
public:
  int face[6];
  Cube() {}
  void roll_z(){ roll(1, 2, 4, 3);}
  void roll_y(){ roll(0, 2, 5, 3);}
  void roll_x(){ roll(0, 1, 5, 4);}    
  
  void roll(int i, int j, int k, int l) {
    int t = face[i];
    face[i] = face[j];
    face[j] = face[k];
    face[k] = face[l];
    face[l] = t;
  }
  
  
  void move(char ch) {
    if(ch == 'E') {
      for(int i = 0; i < 3; i++) roll_y();
    } else if (ch == 'W') {
      roll_y();
    } else if (ch == 'N') {
      roll_x();
    } else if (ch == 'S') {
      for(int i = 0; i < 3; i++) roll_x();
    }
    
  }
  
};

int main() {
  Cube c;
  string ord;

  for(int i = 0; i < 6; i++) cin >> c.face[i];
  cin >> ord;

  for(int i= 0; i < ord.size(); i++) c.move(ord[i]);

  cout << c.face[0] << endl;

  return 0;
}
