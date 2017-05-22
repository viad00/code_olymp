//#include <iostream>
#include <graphics.h>
#include <conio.h>

using namespace std;
void Tr ( int x, int y, int c ) {
         moveto ( x, y );
         lineto ( x, y-60 );
         lineto ( x+100, y );
         lineto ( x, y );
         setfillstyle ( 1, c );
         floodfill ( x+20, y-20, 15 );
    }
main() {
           initwindow (400, 300);
           Tr (100, 100, 14);
           Tr (200, 100, 14);
           Tr (200, 160, 14);
           system (" pause ");
           closegraph();
           return 0; 
}
