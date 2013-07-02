#include <iostream>
#include <sstream>
#include <map>
#include <string>
#include <vector>
using namespace std;

vector<string> split(string s, char c)
{
    vector<string> res;
    stringstream ss;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == c)
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
    map<string, string> trans;
    string line;
    vector<string> sp;
    while (true)
    {
        getline(cin, line);
        if (line == "text:") break;

        sp = split(line, '=');
        trans[sp[0]] = sp[1];
    }

    getline(cin, line);

    sp = split(line, ' ');
    for (int i = 0; i < sp.size(); i++)
    {
        if (i != 0) cout << " ";
        cout << trans[sp[i]];
    }

    cout << endl;

    return 0;
}
