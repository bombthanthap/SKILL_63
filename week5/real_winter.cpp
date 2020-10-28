#include <iostream>
using namespace std;
bool isPrime(int num);

int main(){
   int n,k;
   cin>>n>>k;
   int ar[n],hit=k;
   for(int i=0;i<n;i++){
   		cin>>ar[i];
   }
   for(int i=0;i<n;i++){
   		if(isPrime(ar[i])){
   			hit=k;
		   }
		else{
			hit--;
		}
		if(hit<0){
			cout<<"NO";
			exit(0);
		}
   }
   cout<<"YES";
   return 0;
}
bool isPrime(int num){
    bool flag=true;
    for(int i = 2; i <= num / 2; i++) {
       if(num % i == 0) {
          flag = false;
          break;
       }
    }
    return flag;
}
