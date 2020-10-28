#include<iostream>
#include <algorithm> 
using namespace std;
int main() 
{ 
	int n,t,sum=0;
	cin >> n>>t;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	} 
	sort(arr,arr+n);
	
    for (int i = 0; i < t; ++i) 
    	sum+=arr[n-i-1];
//        cout << arr[n-i-1] << " "; 
	cout<<sum;
    return 0; 
} 
