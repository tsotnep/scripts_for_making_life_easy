nclude <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <iomanip>
using namespace std;

//VISUALLY see how many weeks left for you to live.

//clear; g++ weeks.cpp && ./a.out


int main() {
    int age = 24;
    int deathage = 70;
    int edu = 16;
    int m=52; //weeks in a year


    int lived=age-edu;
    int left= deathage-age;

    cout<<"current age: "<<age<<"\nmaximum age: "<<deathage<<"\n";
    cout<<"'\033[34m+\033[0m' weeks DONE not in education\n";
    cout<<"'\033[31m+\033[0m' weeks DONE in education (12+4 years)\n";
    cout<<"'\033[32m-\033[0m' weeks LEFT to live\n";


    lived*=m;
    edu*=m;
    left*=m;

    string z;

    while(lived--) z+="\033[34m+\033[0m";
    while(edu--) z+="\033[31m+\033[0m";
    while(left--) z+="\033[32m-\033[0m";


    int totweeks=m*deathage, i=0, line=1, ch=8; //totweeks -> total characters(+,-) on a screen; ch -> 8 characters is one colored symbol.

    while(i +1 <= totweeks*ch){
        if (!(i%(140*ch))) {cout<<endl; cout<<setw(2)<<line++;} //i want 140 characters(+,-) on a line
        cout<<z[i];
        i++;
    }

    cout<<endl;
    return 0;
}

