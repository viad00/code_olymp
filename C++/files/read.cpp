//Создатель Владислав Уткин.
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	char s[80];
	ifstream f;
	f.open ("file1.txt");
	f>>s;
	cout<<s<<endl;
	f.close ();
    system ("pause");
    return 0;
}

