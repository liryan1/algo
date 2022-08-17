// Given two sets of points representing rectangles, return whether they overlap.
#include <iostream>
#include <assert.h>
using namespace std;

struct Point {
    int x;
    int y;
};

struct Rect {
    // TR: Top Right. BL: Bottom Left.
    // Coordinates for each rectangle: (x1, y1, x2, y2),
    // where BL = (x1, y1), TR = (x2, y2)
    Point BL;
    Point TR;
};

bool overlap(Rect &R1, Rect &R2)
{
    // Return True if two rectangles overlap.
}

int main() {
    Rect R1 = {{0, 0}, {2, 2}};
    Rect R2 = {{1, 1}, {3, 3}};
    assert(overlap(R1, R2) == true);
    cout << "----- Test1 passed." << endl;
    
    R1 = {{0, 0}, {1, 1}};
    R2 = {{1, 0}, {2, 1}};
    assert(overlap(R1, R2) == false);
    cout << "----- Test2 passed." << endl;

    R1 = {{0, 0}, {100, 1}};
    R2 = {{0, 1}, {100, 2}};
    assert(overlap(R1, R2) == false);
    cout << "----- Test3 passed." << endl;
}