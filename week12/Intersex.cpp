#include<iostream>
#include<stdio.h>
#include<algorithm> 

using namespace std;

int main()
{
	int n, i = 0, j = 0, k = 0;
	int count= 0;
	
	cin >> n;
	
	int A[n];
	int B[n];
	
	
	for(int k = 0 ; k <= n-1 ; k++)
	{
		cin >> A[k];
	}
	
	for(int k = 0 ; k <= n-1 ; k++)
	{
		cin>>B[k];
	}
	
	sort(A,A+n); 
	sort(B,B+n); 
	
	while( i < n && j < n)
	{
		if(A[i] == B[j])
		{
			i = i+1;
			j = j+1;
			count = count+1;			
		}
		else
		{
			if (A[i] < B[j])
			{
				i = i+1;
			}
			else
			{
				j = j+1;
			}	
		}
	} 
	 
	cout << count;
}
