#include <iostream>

using namespace std;

int main() {
    double x, l;
    cout<<"Цена за квадратный метр линолиума:";
    cin>>l;
    cout<<"Введите длину куска:";
    cin>>x;
    cout<<"Стоимость куска =";
    cout<<3.05/l*x<< endl;

    system ("pause");
    return 0;
}
