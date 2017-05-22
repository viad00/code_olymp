//Создатель Владислав Уткин.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	int i,x,y;
	for (x=1; x<=9; x++) {
		for (y=1; y<=9; y++) {
			 i=((x*10000+1022)*10)+y;
			 if (i%7==0 && i%8==0 && i%9==0)
	         cout <<i<<endl;
		}
	}
    system ("pause");
    return 0;
}

