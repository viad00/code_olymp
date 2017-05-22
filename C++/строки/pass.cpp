#include <iostream>
#include <cstring>
#include <cstdio>
#include <cctype>

using namespace std;

int main() {
    char parol[7]="qwerty", p[20];
    cout <<"Введите пароль:\n>";
    gets (p);
    if(strcmp(parol,p)!=0){
          cout <<"Неверный пароль\n";
          system ("pause");
          return 0;
    }
    cout <<"Доступ разрешён!\n";
    char s[70];
    cout <<"Ведите фразу:\n>";
    gets (s);
    int n=strlen(s), k=0;
    for (int i=0; i<n-1; i++) {
        if (s[i]==' '&&s[i+1]!=' ') k++;
    }
    cout<<"Кол-во слов: "<<k+1<<endl;
    system ("pause");
    return 0;
}
