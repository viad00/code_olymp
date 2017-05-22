#include <iostream>

using namespace std;

int main() {
    int TABL[11][11], sum=0;
    for (int i=1; i<=10; i++) {
    for (int j=1; j<=10; j++) {
		TABL[i][j]=1;
		cout << TABL[i][j] << " ";
	}
    cout <<endl;
    }
    cout <<endl;
    for (int i=1; i<=10; i++) {
        TABL[i][1]=i;
        for (int j=i; j<=10; j++) {
            TABL[i][j]=i*j;
            if (TABL[i][j]%3==0) sum=sum+1;
        }
    }
    for (int i=1; i<=10; i++) {
    for (int j=1; j<=10; j++) {
		cout << TABL[i][j] << " ";
	}
    cout <<endl;
    }
    cout <<endl<<sum<<endl;
    system ("pause");
    return 0;
}
