#include <iostream>
#include <graphics.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main() {
    int y=150;
    double h;
    srand(time(NULL));
    initwindow(300,300);
    setfillstyle(1,15);
    bar(0,0,300,300);
    setcolor(0);
    for(int i=100; i>6; i=i-5) {
            y=y+5;
            circle (150,y,i);
            setfillstyle(1,(1+rand()%255, 1+rand()%255, 1+rand()%10));
            floodfill(150,y,0);
    }
    system ("pause");
    return 0;
}
