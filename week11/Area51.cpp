#include <iostream>
#include <stdio.h>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	int x1,y1,w1,h1;
	int x2,y2,w2,h2;
	
	cin>>x1>>y1>>w1>>h1;
	cin>>x2>>y2>>w2>>h2;
	
	int OverlapX = max(0,(min(x1 + w1,x2 + w2) - max(x1,x2)));
 	int OverlapY = max(0,(min(y1 + h1,y2 + h2) - max(y1,y2)));
 	
	if(OverlapX*OverlapY>0)
	{
	 	cout<< (w1*h1) + (w2*h2) - (OverlapX*OverlapY);
	}
	else
	{
		cout<<(w1*h1) + (w2*h2);
	}
}

