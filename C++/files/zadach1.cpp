//Создатель Владислав Уткин.
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	int a,b,i,p,var;
	ifstream f;
	f.open("input_1.txt");
	f>>a>>b;
	p=1;
	for (i=1; i<=b; i++) {
		p=p*a;
	}
	f.close ();
	var=p%10;
	ofstream d;
	d.open ("zadacha_1.txt");
	d<<var<<endl;
	d.close ();
	cout<<var<<endl;
    return 0;
}
