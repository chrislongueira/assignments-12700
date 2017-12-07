#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

std::string line(int l, std::string c){

  return "";
}

std::string rect(int w, int h) {
  std::string str;
  for (int i = 0; i < w; ++i){
    str.append("*");
  }
  for (int j = 0; j < h; ++j){
    std::cout << str << std::endl;
  }
  return "";
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  std::string str;
  for (int i = 0; i < h; ++i){
    str.append("*");
    std::cout << str << std::endl;
  }

  return "";
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  for (int i = 1; i < h*2; i = i + 2){
    std::string str = "";
    for (int j = ((h-i)/2)+3; j > 0; --j){
      str.append(" ");
    }
    for (int k = 0; k < i; ++k){
      str.append("*");
    }
    std::cout << str << std::endl;
  }

  return "";
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  for (int i = 0; i < h; ++i){
    std::string newstring = "";
    for (int b = h-i; b > 0; --b){
      newstring.append(" ");
    }
    for (int c = 0; c < i + 1; ++c){
      newstring.append("*");
    }
    std::cout << newstring << std::endl;
  }
 

  return "";
}

int main(){
  rect(5, 3);
  std::cout << "-" << std::endl;
  tri1(6);
  std::cout << "-" << std::endl;
  tri2(3);
  std::cout << "-" << std::endl;
  tri3(4);

  return 0;
}

