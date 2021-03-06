#include <iostream>
#include <string>
#include <locale>

bool is_vowel(char vowel){
  if (vowel == 'a' || vowel == 'e' || vowel == 'i' || vowel == 'o' || vowel == 'u' ){
    return true;
  }
  else{
    return false;
  }
}

std::string piglatinify(std::string word){
  std::string result  = "";
  for (int i = 0; i < word.length(); i++){
    word[i] = tolower(word[i]);
  }
  if (is_vowel(word[0])){
    result  = word + "ay";

  }
  else{
    result = word.substr(1, word.length()) + word[0] + "ay";
  }
  return result;

}

int main(){
  std::string ex1 = piglatinify("elephant");
  std::string ex2 = piglatinify("computer");
  std::string ex3 = piglatinify("Television");
  std::string ex4 = piglatinify("autobiography");

  std::cout << ex1 << std::endl;
  std::cout << ex2 << std::endl;
  std::cout << ex3 << std::endl;
  std::cout << ex4 << std::endl;

}
