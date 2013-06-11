#include <iostream>
using namespace std;

int sumr(int **arr, int n, int x, int y, int dx, int dy)
{
    int s = 0;
    while (0 <= x && 0 <= y && x < n && y < n)
    {
        s += arr[x][y];
        x += dx;
        y += dy;
    }

    return s;
}

int main()
{
    int n;
    cin >> n;
    int **arr = new int*[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = new int[n];
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
        }
    }

    bool ok = true;
    int s = sumr(arr, n, 0, 0, 1, 1);

    for (int i = 0; i < n; i++)
    {
        ok = ok && s == sumr(arr, n, 0, i, 1, 0);
        ok = ok && s == sumr(arr, n, i, 0, 0, 1);
    }

    ok = ok && s == sumr(arr, n, 0, 0, 1, 1);
    ok = ok && s == sumr(arr, n, n-1, 0, -1, 1);

    if (ok)
    {
        cout << "galdraferningur" << endl;
    }
    else
    {
        cout << "ekki galdraferningur" << endl;
    }

    return 0;
}
