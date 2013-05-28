#include <iostream>
using namespace std;

int heildarfjoldi(int kr5000, int kr1000, int kr500)
{
    return 5000 * kr5000 + 1000 * kr1000 + 500 * kr500;
}

int main()
{
    int kr5000, kr1000, kr500;
    cin >> kr5000 >> kr1000 >> kr500;
    cout << heildarfjoldi(kr5000, kr1000, kr500) << endl;
    return 0;
}
