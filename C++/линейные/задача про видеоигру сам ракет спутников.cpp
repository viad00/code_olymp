#include <iostream>

using namespace std;

int main() {
    double a, b, c;
    cout <<"Сколько игрок сбил самолётов, ракет, спутников?\n";
    cin >>a>>b>>c;
    cout <<"Игрок сбил:\n";
    cout <<a<<" самолётов\n";
    cout <<b<<" ракет\n";
    cout <<c<<" спутников\n";
    cout <<"Он набрал "<<(a*50)+(b*100)+(c*200)<<" очков\n";
    system ("pause");
    return 0;
}
