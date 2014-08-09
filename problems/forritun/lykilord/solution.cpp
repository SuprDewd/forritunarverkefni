#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    string line;
    getline(cin, line);

    int cnt = 0;

    if (line.size() >= 8) cnt++;

    bool low = false, high = false, other = false;
    for (int i = 0; i < line.size(); i++)
    {
        if (line[i] >= 'a' && line[i] <= 'z')
        {
            low = true;
        }
        else if (line[i] >= 'A' && line[i] <= 'Z')
        {
            high = true;
        }
        else
        {
            other = true;
        }
    }

    if (low && high) cnt++;

    if ((low || high) && other) cnt++;

    cout << "Lykilorðið er ";

    if (cnt == 0)
    {
        cout << "veikt" << endl;
    }
    else if (cnt == 1)
    {
        cout << "ásættanlegt" << endl;
    }
    else if (cnt == 2)
    {
        cout << "gott" << endl;
    }
    else if (cnt == 3)
    {
        cout << "sterkt" << endl;
    }

    return 0;
}
