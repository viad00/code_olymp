#include <iostream>

using namespace std;

int main() {
    double m;
    cout <<"Введите ваш возраст: \n";
    cin >>m;
    if (m >= 25 && m <= 40)
    cout <<"Поздравляем! Вы приняты на работу.\n";
    else 
    cout <<"Извините вы нам не подходите.\n";
    system ("pause");
    return 0;
}
