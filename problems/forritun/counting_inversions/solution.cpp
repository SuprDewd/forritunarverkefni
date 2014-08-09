#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
  int n;
  cin >> n;

  int A[n];
  for (int i=0; i < n; i++)
    cin >> A[i];

  int inv=0;
  for (int i=0; i < n; i++)
    for (int j=i+1; j < n; j++)
      if (A[j] < A[i])
	inv++;

  cout << inv << endl;
}
