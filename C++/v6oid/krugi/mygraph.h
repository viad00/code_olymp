#include <graphics.h>
#include <conio.h>
#include <stdlib.h>

void krugi ( int x, int y, int r, int c) {
    for(int i=r; i>6; i=i-5) {
            y=y+5;
            circle (x,y,i);
            setfillstyle(1, c);
            floodfill(x,y,15);
    }
}
