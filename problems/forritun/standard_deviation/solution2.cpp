//Tomas Ken Magnusson
//tomasm12@ru.is
//16.10.2012
//Program calculate the standard deviation of maximum 10 numbers.

#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;

void FillArray(double numbers[], int n);
double findAverage(double numbers[], int n);
double Standard(double numbers[], int n, double average);

int main()
{
    int N;
    cin >> N;
    double numbers[10];

    FillArray(numbers, N);

    double Average = findAverage(numbers, N);
    cout << Standard(numbers, N, Average) << endl;
    return 0;
}
double findAverage(double numbers[], int n)
{
    double sum = 0.0;
    for(int i=0;i<n;i++)
        sum += numbers[i];
    return sum / (double)n;
}
double Standard(double numbers[], int n, double average)
{
    double sum = 0.0;
    for(int i=0;i<n;i++)
        sum += (numbers[i] - average)*(numbers[i] - average);
    return sqrt(sum/n);
}
void FillArray(double numbers[], int n)
{
    for(int i=0;i<n;i++)
        cin >> numbers[i];
}
