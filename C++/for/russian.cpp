//���������: ��������� �����.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	char n;
	cout <<"������� �� ���������� c++\n 1. if\n 2. switch\n 3. for\n�������� ���� �� ���������.";
	cin >>n;
	switch (n) {
		case '1': cout <<"�������� if:\n if (�������) �����������;\n esle �����������;\n"; break;
		case '2': cout <<"�������� switch:\n switch (���������)\n {\n case ���������: ������������������ �����������;\n break;\n ...\n default: ���� ����� �����������\n }\n"; break;
		case '3': cout <<"�������� for:\n for (�������������; �������; �����������)\n  �����������;\n"; break;
		default : cout <<"����������� ��������.\n"; break;
	}
    system ("pause");
    return 0;
}

