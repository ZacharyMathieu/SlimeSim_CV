//
// Created by zwazo on 2022-09-24.
//

#ifndef SLIMESIMAPP_PHEROMONE_H
#define SLIMESIMAPP_PHEROMONE_H

#include "EnvironmentData.h"

#include <string>

class Pheromone {
public:
    double level = 0;
    bool active = true;
    bool needHighlight = false;

    Pheromone(EnvironmentData *data);

    long slimeId;

    void addSlimeLevel();

    void diffuse();

    void highlight();

    bool lowlight();

    void deactivate();
private:
    EnvironmentData *envData;
};


#endif //SLIMESIMAPP_PHEROMONE_H
