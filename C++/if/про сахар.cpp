#include <iostream>

using namespace std;

int main() {
    double m, n;
    cout <<"Введите массу первого и второго пакета.\n";
    cin >>m>>n;
    cout <<"Пакет с наибольшей массой: ";
    if (m > n){
    cout <<"Первый\n";
    cout <<"Его масса: "<<m<<endl;}
    else {
    cout <<"Второй\n";
    cout <<"Его масса: "<<n<<endl;};
    system ("pause");
    return 0;
}
