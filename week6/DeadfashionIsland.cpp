#include<stdio.h>
#include<iostream>
using namespace std;

int main(){
	int H,W,count;
	
	cin >> W >> H;
	
	int Arr[H][W];
	
	for(int i = 0;i < H;i++){
		
		for(int j = 0;j < W;j++){
			cin >> Arr[i][j];
		}
	}
	
	for(int i = 0;i < H;i++){
		
		for(int j = 0;j < W;j++){
			
			if(Arr[i][j] == 1){
				count = 0;
				
				for(int m = i - 1;m <= i + 1;m++){
					
					for(int n = j - 1;n <= j + 1;n++){
						
						if(Arr[m][n] == 1){
							count++;
						}
					}
				}
				
				if(count < 3){
					cout << "No" << endl;
					return 0;
				}
			}
		}
	}
	
	cout << "Yes" << endl;
}
