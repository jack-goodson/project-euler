//
//  main.cpp
//  Euler9
//
//  Created by Jack Goodson on 1/06/20.
//  Copyright © 2020 Jack Goodson. All rights reserved.
//  This is the solution for the 9th problem in the Euler project
//  problem set

#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main() {
    for(int a = 1; a <= 1000; ++a){
        int a_sq = pow(a, 2);
        for(int b = 1; b <= 1000; ++b){
            int b_sq = pow(b, 2);
            for(int c = 1; c <= 1000; ++c){
                int c_sq = pow(c, 2);
                int a_sq_plus_b_sq = a_sq + b_sq;
                if (a < b && b < c && (c_sq == a_sq_plus_b_sq) && ((a+b+c) == 1000)){
                    cout << a * b * c;
                    return 0;
                }
            }
        }
    }
}
