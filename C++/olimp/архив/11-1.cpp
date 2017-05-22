#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int T, N;
	ifstream d;
	d.open ("input.txt");
	d>>N;
	d>>T;
	double Ai[N], result[N];
	int Bi[N], Ci[N];
	for (int i=1; i<=N; i++) {
		d>>Ai[i];
		d>>Bi[i];
		d>>Ci[i];
		result[i]=T*Ai[i]+Bi[i]+Ci[i];
	}
	double end=result[1], k2;
	for (int i=1; i<=N; i++) {
		if (result[i]<=end) {
			end=result[i];
			k2=i;
	    }
	}
	cout <<"Архив суммарное время передачи сообшения которого будет минимальный - "<<k2<<"\n";
	d.close();
	ofstream f;
	f.open("output.txt");
	f<<k2;
	f.close();
	system ("pause");
	return 0;
}
