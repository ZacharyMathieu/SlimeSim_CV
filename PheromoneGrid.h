//
// Created by zwazo on 2022-09-24.
//

#ifndef SLIMESIMAPP_PHEROMONEGRID_H
#define SLIMESIMAPP_PHEROMONEGRID_H

#include "EnvironmentData.h"
#include "Pheromone.h"

#include <vector>
#include <string>

class PheromoneGrid {
private:
    std::vector<std::vector<Pheromone*>> *grid;
    EnvironmentData *envData;
public:
    explicit PheromoneGrid(int width, int height, EnvironmentData *data);

    void update();

    void addSlimeLevel(int x, int y);

    void setSlimeId(int x, int y, long id);

    std::vector<std::vector<Pheromone*>> *getGrid();

    void updateSize();
};

#endif //SLIMESIMAPP_PHEROMONEGRID_H
