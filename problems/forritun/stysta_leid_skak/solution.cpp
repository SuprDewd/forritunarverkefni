#include <iostream>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;

typedef pair<int, int> ii;

int main()
{
    string a, b;
    cin >> a >> b;

    int sx = a[0] - 'a',
        sy = a[1] - '1',
        tx = b[0] - 'a',
        ty = b[1] - '1';

    ii back[8][8];
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            back[i][j] = ii(-1, -1);
        }
    }

    queue<ii> Q;
    Q.push(ii(sx, sy));
    back[sx][sy] = ii(sx, sy);

    while (!Q.empty())
    {
        ii cur = Q.front(); Q.pop();

        for (int i = -2; i <= 2; i++)
        {
            for (int j = -2; j <= 2; j++)
            {
                if ((abs(i) == 1 && abs(j) == 2) || (abs(i) == 2 && abs(j) == 1))
                {
                    int nx = cur.first + i,
                        ny = cur.second + j;

                    if (nx >= 0 && ny >= 0 && nx < 8 && ny < 8 && back[nx][ny].first == -1)
                    {
                        back[nx][ny] = cur;
                        Q.push(ii(nx, ny));
                    }
                }
            }
        }
    }

    stack<ii> path;
    path.push(ii(tx, ty));

    int cnt = 0;
    while (path.top() != ii(sx, sy))
    {
        ii last = path.top();
        ii nxt = back[last.first][last.second];
        path.push(nxt);
        cnt++;
    }

    cout << cnt << endl;
    bool first = true;
    while (!path.empty())
    {
        if (first) first = false;
        else cout << " ";
        ii cur = path.top(); path.pop();
        cout << static_cast<char>('a' + cur.first) << (cur.second + 1);
    }

    cout << endl;
    return 0;
}
