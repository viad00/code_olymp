using System;
using System.IO;

namespace A_Yadra
{
	class MainClass
	{
		public static void Main(string[] args)
		{
			FileStream fs = new FileStream("distance.out", FileMode.Create);
			TextWriter tmp = Console.Out;
			StreamWriter sw = new StreamWriter(fs);
#if DEBUG
			Console.SetOut(tmp);
#else
			Console.SetOut(sw);
#endif
			FileStream ii = new FileStream("distance.in", FileMode.Open);
			TextReader tmpi = Console.In;
			StreamReader swi = new StreamReader(ii);
#if false
			Console.SetIn(tmpi);
#else
			Console.SetIn(swi);
#endif
			//Here comes the plane
			string s1 = Console.ReadLine();
			string s2 = Console.ReadLine();
			int[,] D = new int[s1.Length + 1, s2.Length + 1];
			D[0, 0] = 0;
			for (int j = 1; j <= s2.Length; j++)
			{
				D[0, j] = D[0, j - 1] + 1;
			};
			for (int i = 1; i <= s1.Length; i++)
			{
				D[i, 0] = D[i - 1, 0] + 1;
				for (int j = 1; j <= s2.Length; j++)
				{
					if (s1[i-1] != s2[j-1])
					{
						D[i, j] = Math.Min(D[i - 1, j] + 1, Math.Min(D[i, j - 1] + 1, D[i - 1, j - 1] + 1));
					}
					else
					{
						D[i, j] = D[i - 1, j - 1];
					};
				};
			};
			Console.WriteLine(D[s1.Length, s2.Length]);
			//ENDS
			sw.Close();
			swi.Close();
		}
	}
}
