#include <iostream>
#include <graphics.h>
#include <conio.h>

using namespace std;

int main() {
    initwindow(300,300);
    setfillstyle(1,4);
    bar(50,50,150,100);
    line(50,50,50,200);
    system ("pause");
    closegraph();
    return 0;
}
