#include <iostream>
#include <graphics.h>
#include <conio.h>

using namespace std;

int main() {
    int windows[2],dom[4],roof[6];
    initwindow(300,300);
    dom[1]=100;
    dom[2]=100;
    dom[3]=200;
    dom[4]=200;
    dom[0]=7;
    windows[0]=9;
    windows[1]=150;
    windows[2]=150;
    roof[0]=4;
    roof[1]=100;
    roof[2]=100;
    roof[3]=150;
    roof[4]=50;
    roof[5]=200;
    roof[6]=100;
    setfillstyle(1,dom[0]);
    bar(dom[1],dom[2],dom[3],dom[4]);
    setcolor(0);
    circle(windows[1],windows[2],30);
    setfillstyle(1,windows[0]);
    floodfill(windows[1],windows[2],0);
    setcolor(15);
    moveto(roof[1],roof[2]);
    lineto(roof[3],roof[4]);
    lineto(roof[5],roof[6]);
    lineto(roof[1],roof[2]);
    setfillstyle(1,roof[0]);
    floodfill(roof[1]+10,roof[2]-2,15);
    system ("pause");
    closegraph();
    return 0;
}
