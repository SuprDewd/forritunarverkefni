#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <ciso646>
using namespace std;

vector<string> split(string s, char c)
{
    vector<string> res;
    stringstream ss;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == ' ')
        {
            res.push_back(ss.str());
            ss.str("");
        }
        else
        {
            ss << s[i];
        }
    }

    res.push_back(ss.str());
    return res;
}

int main()
{
    string line;
    getline(cin, line);

    vector<string> sp = split(line, ' ');

    bool found = false;
    for (int i = 0; i < sp.size(); i++)
    {
        if (sp[i] == "") continue;

        bool ok = true;
        for (int j = 0; j < sp[i].size(); j++)
        {
            if (j == 0 && sp[i][j] == '-') continue;
            if (sp[i][j] < '0' || sp[i][j] > '9')
            {
                ok = false;
            }
        }

        if (ok)
        {
            found = true;
        }
    }

    if (found)
    {
        cout << "Já" << endl;
    }
    else
    {
        cout << "Nei" << endl;
    }

    return 0;
}
