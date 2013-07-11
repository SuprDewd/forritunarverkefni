#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int arr[10][5][3] = {
    {
        {1, 1, 1},
        {1, 0, 1},
        {1, 0, 1},
        {1, 0, 1},
        {1, 1, 1},
    },
    {
        {0, 0, 1},
        {0, 0, 1},
        {0, 0, 1},
        {0, 0, 1},
        {0, 0, 1},
    },
    {
        {1, 1, 1},
        {0, 0, 1},
        {1, 1, 1},
        {1, 0, 0},
        {1, 1, 1},
    },
    {
        {1, 1, 1},
        {0, 0, 1},
        {1, 1, 1},
        {0, 0, 1},
        {1, 1, 1},
    },
    {
        {1, 0, 1},
        {1, 0, 1},
        {1, 1, 1},
        {0, 0, 1},
        {0, 0, 1},
    },
    {
        {1, 1, 1},
        {1, 0, 0},
        {1, 1, 1},
        {0, 0, 1},
        {1, 1, 1},
    },
    {
        {1, 1, 1},
        {1, 0, 0},
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1},
    },
    {
        {1, 1, 1},
        {0, 0, 1},
        {0, 0, 1},
        {0, 0, 1},
        {0, 0, 1},
    },
    {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1},
    },
    {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1},
        {0, 0, 1},
        {0, 0, 1},
    }
};

int main()
{
    string n;
    cin >> n;

    vector<int> num;
    stack<int> tmp;

    for (int i = 0; i < n.size(); i++)
    {
        num.push_back(n[i] - '0');
    }

    // if (n == 0)
    // {
    //     num.push_back(0);
    // }
    // else
    // {
    //     while (n)
    //     {
    //         tmp.push(n % 10);
    //         n /= 10;
    //     }

    //     while (!tmp.empty())
    //     {
    //         num.push_back(tmp.top());
    //         tmp.pop();
    //     }
    // }

    for (int row = 0; row < 5; ++row)
    {
        for (int i = 0; i < num.size(); i++)
        {
            if (i != 0)
            {
                cout << " ";
            }

            for (int col = 0; col < 3; col++)
            {
                cout << (arr[num[i]][row][col] ? "@" : " ");
            }
        }

        cout << endl;
    }

    return 0;
}
