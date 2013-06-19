#include<iostream>
#include<iomanip>
#include<limits.h>

using namespace std;

int main()
{
    int times, nums, min, max, temp, sum;
    cin >> times;
    while(times--)
    {
        max = INT_MIN;
        min = INT_MAX;
        sum = 0;
        cin >> nums;
        for(int i = 0; i != nums; i++)
        {
            cin >> temp;
            if(temp > max)
            {
                max = temp;
            }
            if(temp < min)
            {
                min = temp;
            }
            sum += temp;
        }
        cout << "Max: " << max << endl;
        cout << "Min: " << min << endl;
        cout << "Average: " << fixed << setprecision(2) << static_cast<double>(sum)/nums << endl;
        if(times != 0)
        {
            cout << endl;
        }
    }
    return 0;
}
