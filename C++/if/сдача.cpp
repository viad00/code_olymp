#include <iostream>
#include <cstring>
#include <cctype>
#include <cstdio>

using namespace std;

int main() {
    char s[80];
    cout <<"�������:\n>";
    gets (s);
    int i=0;
    while (s[i]!='\0') {
        if (s[i]=='a') s[i]='b';
        else if (s[i]=='b') s[i]='a';
        if (s[i]=='A') s[i]='B';
        else if (s[i]=='B') s[i]='A';
        i++;
    }
    cout <<"���������: "<<s<<endl;
    system ("pause");
    return 0;
}
                                                   ��   >�8����S�}�q�����2� R�Í���Ϻ敠��0/�8�i��0��8�@z�ؾb�Y�)ܴnCaPs�M������*I�`Z�b�D��K*�`epoz������,+^@5��%MG�5#�w���#