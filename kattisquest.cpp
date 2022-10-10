#include <iostream>
#include <map>   // https://en.cppreference.com/w/cpp/container/map
#include <queue> // https://en.cppreference.com/w/cpp/container/priority_queue

using namespace std;

map<int, priority_queue<int>> quests;

int session(int _energy)
{
    int gold = 0;
    int energy = _energy;

    for (int j=_energy; j>0; --j)
    {
        if ( quests.find(j) != quests.end() )
        {
            int reward = quests.at(j).top();
                         quests.at(j).pop();

            if (quests.at(j).empty())
                quests.erase(j);

            energy -= j;
            j = energy + 1;
            gold += reward;
        }
    }
    return gold;
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i)
    {
        string action;
        cin >> action;

        if (action.compare("add") == 0)
        {
            int energy, gold;
            cin >> energy >> gold;

            if (!quests.count(energy))
            {
                priority_queue<int> pq;
                quests.insert(pair<int, priority_queue<int>>(energy, pq ));
            }
            quests.at(energy).push( gold );
        }
        else
        {
            int energy;
            cin >> energy;

            int gold = session(energy);
            cout << gold << endl;
        }
    }
    return 0;
}