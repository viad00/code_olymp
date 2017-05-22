//Создатель Владислав Уткин.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	int x,y;
	for (x=1; x<=9; x++) {
		for (y=1; y<=9; y++) {
			if ((x*x*x*x*x)+(y*y*y*y*y)==1025) {
				cout <<x<<"^5+"<<y<<"^5=1025\n";
			}
		}
	}
    system ("pause");
    return 0;
}

