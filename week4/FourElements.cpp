#include<iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int Arr[n];
	for(int i = 0;i < n;i++)
		{
			cin >> Arr[i];
		}
	int x;
	int Sum;
	cin >> x;
	for(int i = 0;i < n-3;i++)
	{
		for(int j = i+1;j < n-2;j++)
		{
			for(int k = j+1;k < n-1;k++)
			{
				for(int l = k+1;l < n;l++)
				{
					Sum = Arr[i]+Arr[j]+Arr[k]+Arr[l];
					if ( Sum == x)
					{
						cout << "YES" <<endl;
						exit(0);
					}
				}
			}
		}
	}
	cout << "NO" <<endl;
	exit(0);
	
}
