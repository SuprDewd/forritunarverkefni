#include <iostream>
#include <string>
#include <ciso646>
using namespace std;

int main()
{
    string line;
    getline(cin, line);

    int n = 'z' - 'a' + 1;
    int cnt[n];
    for (int i = 0; i < n; i++) cnt[i] = 0;

    int words = 0, curlen = 0;
    for (int i = 0; i < line.size(); i++)
    {
        if (line[i] == ' ' || line[i] == '.' || line[i] == ',')
        {
            if (curlen > 0)
            {
                words++;
            }

            curlen = 0;
        }
        else
        {
            curlen++;
            if (line[i] >= 'A' && line[i] <= 'Z')
            {
                cnt[line[i] - 'A']++;
            }
            else
            {
                cnt[line[i] - 'a']++;
            }
        }
    }

    if (curlen > 0)
    {
        words++;
    }

    cout << words << " words" << endl;

    for (int i = 0; i < n; i++)
    {
        if (cnt[i] > 0)
        {
            cout << cnt[i] << " " << static_cast<char>('a' + i) << endl;
        }
    }

    return 0;
}
