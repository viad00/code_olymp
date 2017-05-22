#include <cstdlib>
#include <iostream>
#include "mygraph.h"

using namespace std;

int main(int argc, char *argv[])
{
    initwindow (500, 500);
    krugi (250, 250, 150, 6); // X, Y, R, Color.
    system("PAUSE");
    closegraph();
    return EXIT_SUCCESS;
}
