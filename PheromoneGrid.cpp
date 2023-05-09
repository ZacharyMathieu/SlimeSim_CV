//
// Created by zwazo on 2022-09-24.
//

#include "PheromoneGrid.h"
#include "Random.h"

#include <iostream>

PheromoneGrid::PheromoneGrid(int width, int height, EnvironmentData *data) {
    envData = data;

    updateSize();

    for (int i = 0; i < envData->random_natural_pheromones_count; i++) {
        int x = (int) (Random::getRandomDouble() * width);
        int y = (int) (Random::getRandomDouble() * height);

        grid->at(y).at(x)->deactivate();
        grid->at(y).at(x)->level = envData->natural_pheromones_strength;
    }
}

void PheromoneGrid::update() {
    for (std::vector<Pheromone*> &line: *grid) {
        for (Pheromone *pheromone: line) {
            pheromone->diffuse();
        }
    }
}

void PheromoneGrid::addSlimeLevel(int x, int y) {
    grid->at(y).at(x)->addSlimeLevel();
}

void PheromoneGrid::setSlimeId(int x, int y, long id) {
    grid->at(y).at(x)->slimeId = id;
}

std::vector<std::vector<Pheromone*>> *PheromoneGrid::getGrid() {
    return grid;
}

void PheromoneGrid::updateSize() {
    grid = new std::vector<std::vector<Pheromone*>>();

    for (int y = 0; y < envData->grid_height; y++) {
        std::vector<Pheromone*> v = std::vector<Pheromone*>();

        for (int x = 0; x < envData->grid_width; x++) {
            v.push_back(new Pheromone(envData));
        }
        grid->push_back(v);
    }
}
