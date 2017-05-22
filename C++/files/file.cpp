//Создатель Владислав Уткин.
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	ofstream f;
	f.open ("file1.txt");
	f<<"write_in_file._author_utkin";
	f.close ();
    return 0;
}

