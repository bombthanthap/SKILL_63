#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{    
    int n,x;
    int Max = 0,Row = 0,Col = 0;
    int count = 0;
    bool check;
    
    
    cin >> n;
    char Arr[1000][1000];
    
    for(int i = 0;i < n;i++)
    {
    	
        for(int j = 0;j < n;j++)
        {
            cin>>Arr[i][j];
        }
    }
    
    for(int i = 0;i < n;i++)
    {
    	
        for(int j = 0;j < n;j++)
		{
			
        	if(Arr[i][j] != '0')
			{
        		count = 0;
                check = true;
                
                while(check)
                {
                	count++;
                	
                	if(i + count >= n)
					{
                		check = false;
					}
					
					if(j + count >= n)
					{
						check = false;
					}
					
					if(check)
					{
						
						for(int x = 0;x <= count;x++)
						{
							
							if(Arr[i+x][j+count] == '0')
							{
								check = false;
							}
							
							if(Arr[i+count][j+x] == '0')
							{
								check = false;
							}
						}
					}
				}
				
                if(count > Max)
                {
                	Max = count;
                	Row = i;
                	Col = j;
				}
            }
        }
    }
    
	cout << Row + 1 << " " << Col + 1 << endl;
	cout << Max * Max; 
}
