//���������: ��������� �����.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	int sum, k, ball; double srednee;
	sum = 0; k=1;
	while (k<=10) {
		cout <<"������� ������:\n>";
		cin >>ball;
		if (ball <= 100 && ball >= 0) {
			sum=sum+ball;
			k++;
		}
		else
		cout <<"��� �� ����� ���� �������!\n";
	}
	srednee=sum/k;
	cout <<"������� ������ �� ������: "<<srednee<<endl;
    system ("pause");
    return 0;
}

