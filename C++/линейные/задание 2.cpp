//задание 2
#include <iostream>

using namespace std;

int main() {
    int a, b, c, d, n;
    cout <<"цена перчаток"<<endl;
    cin >>a;
    cout <<"цена портфель"<<endl;
    cin >>b;
    cout <<"цена галстек"<<endl;
    cin >>c;
    cout <<"деньги"<<endl;
    cin >>d;
    cout <<"сдача"<<endl;
    n=d-a-b-c;
    cout <<n<<endl;
    system ("pause");
    return 0;
}
