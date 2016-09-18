#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    int road; // the length of the road before the gap.
    cin >> road; cin.ignore();
    int gap; // the length of the gap.
    cin >> gap; cin.ignore();
    int platform; // the length of the landing platform.
    cin >> platform; cin.ignore();
    int lpr = {0+road-1};
    int lpg = {0+road+gap-1};
    int lpp = {0+road+gap+platform-1};

    // game loop
    while (1) {
        int speed; // the motorbike's speed.
        cin >> speed; cin.ignore();
        int coordX; // the position on the road of the motorbike.
        cin >> coordX; cin.ignore();

        if ((speed != (gap+1)) && (coordX < lpg)){

            if (speed < (gap+1)){

                cout << "SPEED" << endl;

            } else {

                cout << "SLOW" << endl;

            }

        } else {

            if (((coordX + speed) > lpr) && (coordX < lpg)){

                cout << "JUMP" << endl;

            } else if (coordX > lpg){

                cout << "SLOW" << endl;

            } else {

                cout << "WAIT" << endl;

            }

        }

    }
}