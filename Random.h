//
// Created by zwazo on 2022-09-24.
//

#ifndef SLIMESIMAPP_RANDOM_H
#define SLIMESIMAPP_RANDOM_H

#include <random>
#include <cmath>

class Random {
public:
    static int getRandomInt() {
        std::random_device d;
        return abs((int) d());
    }

    static double getRandomDouble() {
        return (double) (Random::getRandomInt() % 1000) / 1000;
    }

    static bool getRandomBool(double trueOdds) {
        return getRandomDouble() < trueOdds;
    }
};

#endif //SLIMESIMAPP_RANDOM_H
