#include <iostream>
#include <cstdio>
using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
    int n;
    cin >> n;

    if (n % 2 == 0 || n < 1 || n > 19)
    {
        cout << "Ekki lögleg stærð!" << endl;
    }
    else
    {
        int **res = new int*[n];
        for (int i = 0; i < n; i++)
        {
            res[i] = new int[n];
        }

        int x = n/2, y = n/2, d = 1, cur = 0;
        res[x][y] = cur++;
        for (int i = 1; i <= n && cur < n*n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                x += dx[d];
                y += dy[d];
                res[x][y] = cur++;
                if (cur == n*n) break;
            }

            if (cur == n*n) break;
            d = (d + 3) % 4;

            for (int j = 0; j < i; j++)
            {
                x += dx[d];
                y += dy[d];
                res[x][y] = cur++;
                if (cur == n*n) break;
            }

            d = (d + 3) % 4;
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                printf("%5d", res[i][j]);
            }

            printf("\n");
        }

        for (int i = 0; i < n; i++)
        {
            delete[] res[i];
        }

        delete[] res;
    }

    return 0;
}
