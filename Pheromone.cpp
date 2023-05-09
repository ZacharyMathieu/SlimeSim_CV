//
// Created by zwazo on 2022-09-24.
//

#include "Pheromone.h"

Pheromone::Pheromone(EnvironmentData *data) {
    envData = data;
}

void Pheromone::addSlimeLevel() {
    if (active) {
        level += envData->slime_pheromone_level;
        if (level > envData->pheromone_max_level) level = envData->pheromone_max_level;
    }
}

void Pheromone::diffuse() {
    if (active && level > 0) {
        if (envData->pheromone_max_level < level) level = PHEROMONE_MAX_LEVEL_RESET_VALUE;
        level -= envData->pheromone_low_level_diffusion_multiplier * ((1 / (level + 1)) - (1 / (envData->pheromone_low_level_diffusion_multiplier + 1)));
        level -= (envData->pheromone_high_level_diffusion_multiplier * (level / envData->pheromone_max_level)) / envData->pheromone_max_level;
        level -= envData->pheromone_diffusion_constant;
        if (level < 0) level = 0;
    }
}

void Pheromone::highlight() {
    needHighlight = true;
}

bool Pheromone::lowlight() {
    if (needHighlight) {
        needHighlight = false;
        return true;
    }
    return false;
}

void Pheromone::deactivate() {
    active = false;
}
