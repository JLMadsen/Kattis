#include <iostream>
#include <map>   // https://en.cppreference.com/w/cpp/container/map
#include <queue> // https://en.cppreference.com/w/cpp/container/priority_queue

using namespace std;

map<int, priority_queue<int>> quests;

long session(int _energy)
{
    long gold = 0;
    int energy = _energy;

    while (true)
    {
        auto it = quests.upper_bound(energy);
        if (it == quests.begin()) 
            return gold;

        --it;

        gold += it->second.top();
                it->second.pop();

        energy -= it->first;

        if (it->second.empty())
            quests.erase(it->first);
    }
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

            long gold = session(energy);
            cout << gold << endl;
        }
    }
    return 0;
}