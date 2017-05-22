//Создатель: Владислав Уткин.
#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	char n;
	cout <<"Справка по операторам c++\n 1. if\n 2. switch\n 3. for\nВыберите один из вариантов.";
	cin >>n;
	switch (n) {
		case '1': cout <<"Оператор if:\n if (условие) предложение;\n esle предложение;\n"; break;
		case '2': cout <<"Оператор switch:\n switch (выражение)\n {\n case константа: последовательность предложений;\n break;\n ...\n default: Этот пункт отцутствует\n }\n"; break;
		case '3': cout <<"Оператор for:\n for (инициализация; условие; предложение)\n  предложение;\n"; break;
		default : cout <<"Неизвестное значение.\n"; break;
	}
    system ("pause");
    return 0;
}

