#include <iostream>
#include <string>
#include <vector>
#include <ciso646>
using namespace std;

int main()
{
    vector<string> lines;
    string line;
    int mx = 0;
    while (getline(cin, line))
    {
        lines.push_back(line);
        mx = max(mx, static_cast<int>(line.size()));
    }

    for (int i = 0; i < mx; i++)
    {
        for (int j = 0; j < lines.size(); j++)
        {
            if (i < lines[j].size())
            {
                cout << lines[j][i];
            }
            else
            {
                cout << " ";
            }
        }

        cout << endl;
    }

    return 0;
}
