#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double arr[10];
    int n;
    cin >> n;

    double sum = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        sum += arr[i];
    }

    double avg = sum / n;
    sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += pow(arr[i] - avg, 2.0);
    }

    cout << sqrt(sum / n) << endl;
    return 0;
}
