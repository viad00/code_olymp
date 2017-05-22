//Создатель Владислав Уткин.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	char a;
	cout<<"Наберите скоко лет вы ходите на робототехнику от 1 до 3х\n>";
	cin>>a;
	switch (a) {
		case '1': cout <<"Вы пока нормальный человек\n"; break;
		case '2': cout <<"Вы немножко долбаёб\n"; break;
		case '3': cout <<"Вы сказочный далбаёб\n"; break;
		default : cout <<"Вы на стоко даун что даже не можете вбить число от 1 до 3х\n"; break;
	}   
    system ("pause");
    return 0;
}
