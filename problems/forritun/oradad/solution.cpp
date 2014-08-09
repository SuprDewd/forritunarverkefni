#include <iostream>
#include <vector>
#include <algorithm>
#include <ciso646>
using namespace std;

int main()
{
    vector<int> nums;
    int n;
    while (cin >> n)
    {
        nums.push_back(n);
    }

    sort(nums.begin(), nums.end());
    swap(nums[0], nums[1]);

    for (int i = 0; i < nums.size(); i++)
    {
        if (i != 0) cout << " ";
        cout << nums[i];
    }

    cout << endl;

    return 0;
}
