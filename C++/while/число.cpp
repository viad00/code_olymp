//���������: ��������� �����.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	double sum, n;
	sum=0; n=0;
	while (sum<3) {
		cout <<"��� n = "<<n<<", ����� = "<<sum<<endl;
		n++;
		sum = sum+1/n;
	}
	cout <<"\n��� n = "<<n<<", ����� = "<<sum<<endl;
    system ("pause");
    return 0;
}

