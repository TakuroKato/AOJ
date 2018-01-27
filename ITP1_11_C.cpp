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

  int getRight(Cube c1, int f1, int f2) {
    for (int i = 0; i < 6; i++) {
      for (int j = 0; j < 4; j++) {
	if (c1.face[0] == f1 && c1.face[1] == f2) return c1.face[2];
	c1.roll_z();
      }
      if (i % 2 == 0) c1.roll_y();
      else c1.roll_x();
    }
    return -1;
  }
  
};

bool eq(Cube c1, Cube c2) {
  for (int i = 0; i < 6; i++) {
    if (c1.face[i] != c2.face[i]) return false;
  }
  return true;

}

bool equal(Cube c1, Cube c2) {
  for (int i = 0; i < 6; i++) {
    for (int j = 0; j < 4; j++) {
      if(eq(c1,c2)) return true;
      c1.roll_z();
    }
    if(i % 2 == 0) c1.roll_y();
    else c1.roll_x();
  }
  return false;

}

int main() {
  Cube c1,c2;
  for (int i = 0; i < 6; i++) cin >> c1.face[i];
  for (int i = 0; i < 6; i++) cin >> c2.face[i];

  if (equal(c1, c2)) cout << "Yes" << endl;
  else cout << "No" << endl;

  return 0;
}
