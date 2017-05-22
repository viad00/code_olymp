//Создатель Владислав Уткин.
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int i,var;
    
	setlocale(LC_ALL, "Russian");
	ofstream f;
	f.open ("file1.txt");
	for (i=1; i<=9; i++) {
	cout <<"Введите число";
	cin >>var;
    f<<var<<" ";
}
	f.close();
	ifstream d;
	d.open ("file1.txt");
	while (!d.eof()) {
		d>>var;
		cout <<var<<endl;
	}
	
	d.close();
    system ("pause");
    return 0;
}

