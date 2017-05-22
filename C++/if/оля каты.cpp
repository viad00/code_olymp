#include <iostream>

using namespace std;

int main() {
    int a, b;
    cout <<"Введите дату рождения Оли: \n";
    cin >>a;
    cout <<"Введите дату рождения Кати: \n";
    cin >>b;
    if (a>b) cout<<"Катя старше\n";
    if (a == b) cout<<"Даты рождения равны\n";
    if (a<b) cout<<"Оля старше\n";
    system ("pause");
    return 0;
}
