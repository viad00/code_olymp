//Создатель Владислав Уткин.
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main() {
	int n;
	double r,pi,a1,b1,per,a2,b2,a,b;
	per=0;
	ifstream d;
	d.open ("input.txt");
	d>>n;
	d>>r;
	d>>a1;
	d>>b1;
	a=a1;
	b=b1;
	while (!d.eof()) {
		d>>a2;
		d>>b2;
		per=per+(sqrt((a2-a1)*(a2-a1)+(b2-b1)*(b2-b1)));
		a1=a2; b1=b2;
	}
	per=per+sqrt((a1-a)*(a1-a)+(b1-b)*(b1-b)+(a2-a1)*(a2-a1)+(b2-b1)*(b2-b1));
	per=per+((2*3.14*r)/4)*n;
	d.close();
	ofstream f;
	f.open ("output.txt");
	f<<per;
	f.close();
    return 0;
}
