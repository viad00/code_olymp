//Создатель: Владислав Уткин.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	double sum, n;
	sum=0; n=0;
	while (sum<3) {
		cout <<"При n = "<<n<<", сумма = "<<sum<<endl;
		n++;
		sum = sum+1/n;
	}
	cout <<"\nПри n = "<<n<<", сумма = "<<sum<<endl;
    system ("pause");
    return 0;
}

