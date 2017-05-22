#include <iostream>

using namespace std;

int main() {
    double a, b, f;
    cout<<"¬ведите длину стены:";
    cin>>a;
    cout<<"¬ведите высоту стены:";
    cin>>b;
    cout<<"–улон обоев размеров: 12*1"<< endl;
    cout<<"¬ведите цену рулона:";
    cin>>f;
    cout<<(a*b)/(12*1)*f<< endl;
    

    system ("pause");
    return 0;
}
