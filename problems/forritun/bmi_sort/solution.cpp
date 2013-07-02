#include <iostream>
#include <algorithm>
using namespace std;

class person
{
public:
    string name;
    double height;
    double weight;

    double bmi() const {
        return weight / (height * height);
    }
};

bool operator <(const person &a, const person &b) {
    return a.bmi() > b.bmi();
}

int main()
{
    int n;
    cin >> n;
    person *ps = new person[n];
    for (int i = 0; i < n; i++)
    {
        cin >> ps[i].name >> ps[i].height >> ps[i].weight;
    }

    sort(ps, ps + n);
    reverse(ps, ps + n);

    for (int i = 0; i < n; i++)
    {
        cout << ps[i].name << " " << ps[i].bmi() << endl;
    }

    return 0;
}
