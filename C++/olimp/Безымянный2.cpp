#include <iostream>

using namespace std;

int main() {
    int i=12;
    double Nconst;
    for (int N=0; N<=99; N=N++) {
        N=Nconst;
        while (i) {
              if (i%2==0) {
                          Nconst=Nconst*i;
                          i=i-1;
              } else {
                     Nconst=Nconst-i;
                     i=i-1;
              }
        }
        if (Nconst==92161) cout <<Nconst<<" "<<N<<endl;
    }
    system ("pause");
    return 0;
}
