#include <iostream>
#include <cstring>
#include <cctype>
#include <cstdio>

using namespace std;

int main() {
    char s[80];
    cout <<"¬ведите:\n>";
    gets (s);
    int i=0;
    while (s[i]!='\0') {
        if (s[i]>=