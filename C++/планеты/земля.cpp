#include <iostream>
#include <graphics.h>
#include <conio.h>
#include <math.h>
using namespace std;

void earth (int x, int y, int c) {
	const int r=10;
	setcolor(c);
	circle(x,y,r);
	setfillstyle(1, c);
	floodfill (x, y, c);
}

int main () {
	const int rSun=60, L=150, x0=200, y0=200;
	int x,y,code;
	float a, ha;
	initwindow (400,400);
	circle(x0, y0, rSun);
	setfillstyle(1, YELLOW);
	floodfill (x0, y0, WHITE);
	a=0;
	ha= M_PI/180;
	while(1) {
		x=x0+L*cos(a);
		y=y0-L*sin(a);
		earth (x,y, LIGHTBLUE);
		delay(20);
		earth (x,y,0);
		 if (kbhit()) {
			if (27==getch()) break;
		}
		a=a+ha;
	}
	system ("pause");
    return 0;
}
