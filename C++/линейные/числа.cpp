#include <iostream>

using namespace std;

int main() {
    int v, s;
    cout <<"������� ����� �� 5-�� ����:\n";
    cin >>v;
    s=0;
    cout <<v/10000<<"  ";
    s=s+v/10000;
    v=v%10000;
    cout <<v/1000<<"  ";
    s=s+v/1000;
    v=v%1000;
    cout <<v/100<<"  ";
    s=s+v/100;
    v=v%100;
    cout <<v/10<<"  ";
    s=s+v/10;
    v=v%10;
    cout <<v/1<<"\n";
    s=s+v;
    cout <<"����� ���� ����� = "<<s<<endl;
    system ("pause");
    return 0;
}
