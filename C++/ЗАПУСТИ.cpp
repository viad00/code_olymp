//��������� ��������� �����.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	char a;
	cout<<"�������� ����� ��� �� ������ �� ������������� �� 1 �� 3�\n>";
	cin>>a;
	switch (a) {
		case '1': cout <<"�� ���� ���������� �������\n"; break;
		case '2': cout <<"�� �������� ������\n"; break;
		case '3': cout <<"�� ��������� ������\n"; break;
		default : cout <<"�� �� ����� ���� ��� ���� �� ������ ����� ����� �� 1 �� 3�\n"; break;
	}   
    system ("pause");
    return 0;
}
