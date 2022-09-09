#include <deque>
#include <unordered_map>
#include <assert.h>

using namespace std;

class FreqStack
{
public:
    int max_freq = 0;
    unordered_map<int, int> freq;
    unordered_map<int, deque<int>> levels;

    void push(int val) {
        freq[val]++;
        max_freq = max(max_freq, freq[val]);
        levels[freq[val]].push_back(val);
    }

    int pop() {
        int ans = levels[max_freq].back();
        levels[max_freq].pop_back();
        freq[ans]--;
        if (levels[max_freq].size() == 0) {
            max_freq--;
        }
        return ans;
    }
};

int main() {
    FreqStack f;
    f.push(3);
    f.push(4);
    f.push(4);
    f.push(3);
    f.push(5);
    assert(f.pop() == 3);
    assert(f.pop() == 4);
    assert(f.pop() == 5);
    f.push(6);
    f.push(3);
    assert(f.pop() == 3);
    assert(f.pop() == 6);
    assert(f.pop() == 4);
    assert(f.pop() == 3);
}