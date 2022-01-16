#include<iostream.h>
#include<cstdlib.h>
#include<cmath.h>
using namespace std;

int GenPrime(int low, int up){
	bool isPrime(int n){
		if(n<=1)
			return false;
		
		for(int i=2; i<n; i++)
			if(n%1==0)
				return false;
		
		return true;
	}
	int num;
	
	for(int i=low; i<=end; i++){
		num=((rand() % (up + 1 - low)) + low);
		if(isPrime(num))
			break;
		else
			continue;
	}

	return num;
}

int modder(int g, int priv, int n){
	return ((g**priv)%n);
}

int main{
	int low=0, up, g, n;
	int a,b;
	
	cout<<"n, Upper limit:"; cin>>up; n=GenPrime(low, up); cout<<"\nn: "<<n;
	cout<<"g, Upper Limit:"; cin>>up; g=GenPrime(low, up); cout<<"\ng: "<<g;

	cout<<"Private Number 1:"; cin>>a;
	cout<<"Private Number 2:"; cin>>b;

		

	return 0;
}
