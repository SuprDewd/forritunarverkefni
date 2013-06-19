#include <iostream>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    int **arr = new int*[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = new int[n];
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
        }
    }

    int **pat = new int*[m];
    for (int i = 0; i < m; i++)
    {
        pat[i] = new int[m];
        for (int j = 0; j < m; j++)
        {
            cin >> pat[i][j];
        }
    }

    for (int i = 0; i < n - m + 1; i++)
    {
        for (int j = 0; j < n - m + 1; j++)
        {
            int cnt = 0;
            for (int k = 0; k < m; k++)
            {
                for (int l = 0; l < m; l++)
                {
                    if (arr[i + k][j + l] == pat[k][l])
                    {
                        cnt++;
                    }
                }
            }

            if (100 * cnt >= 80 * m * m)
            {
                cout << i << " " << j << endl;
            }
        }
    }

    return 0;
}
