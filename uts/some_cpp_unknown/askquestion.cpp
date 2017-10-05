#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <iostream>
#include <sqlite3.h>

using namespace std;

bool answered = 0;
string one = "";

void oloop() {
        while (!answered) {
                cout << "Enter one" << endl << ">";
                cin >> one;
                if (one == "one") {
                        answered = 1;
                        cout << "Yep!" << endl;
			exit(0);
                } else { cout << "Wrong!" << endl; }
        }
}

void handler(int s) {
        cout << endl << "Don't even try to exit!" << endl;
        oloop();
}

int main(int argc, char** argv) {
   //God save the stackoverflow!
   signal(SIGINT, handler);
   signal(SIGTERM, handler);
   signal(SIGHUP, handler);
   signal(SIGTSTP, handler);
   signal(SIGSTOP, handler);
	
	if (!getenv("SSH_CLIENT")) { exit(0); }
	string env_ip = getenv("SSH_CLIENT");
	
	string cur_ip = "";
	for (int i = 0; i < env_ip.length(); i++) {
		if (env_ip[i] == ' ') { break; }
		cur_ip = cur_ip + env_ip[i];
	}
	cout << "Enter main loop" << endl;
	cout << "Your IP is: " << cur_ip << endl;
	oloop();
	return 0;
}

