//
// Created by zwazo on 2022-09-24.
//

#include "Environment.h"
#include "ParameterReader.h"
#include "Slime.h"

#include <map>
#include <vector>
#include <sstream>
#include <iostream>

Environment::Environment() {
    slimeVector = new std::vector<Slime *>();

    envData = {};

    pheromoneGrid = new PheromoneGrid(envData.grid_width, envData.grid_height, &envData);

    generateRandomSlime(envData.slime_count);
}

int Environment::getWidth() const {
    return envData.grid_width;
}

int Environment::getHeight() const {
    return envData.grid_height;
}

std::size_t Environment::getSlimeCount() {
    return slimeVector->size();
}

std::vector<Slime *> *Environment::getSlimeVector() {
    return slimeVector;
}

PheromoneGrid *Environment::getPheromoneGrid() {
    return pheromoneGrid;
}

void Environment::moveAllSlime() {
    bool seekPheromones = false;

    seekPheromoneTimer++;

    if (seekPheromoneTimer % envData.slime_seek_pheromones_period == 0) {
        seekPheromones = true;
        seekPheromoneTimer = 0;
    }

    for (Slime *slime: *slimeVector) {
        slime->moveForward(pheromoneGrid, getSlimeVector(), seekPheromones);
    }
}

void Environment::updatePheromones() {
    for (Slime *slime: *slimeVector) {
        pheromoneGrid->addSlimeLevel((int) slime->getX(), (int) slime->getY());
        pheromoneGrid->setSlimeId((int) slime->getX(), (int) slime->getY(), slime->getId());
    }

    pheromoneGrid->update();
}

void Environment::physics() {
    moveAllSlime();
    updatePheromones();
}

void Environment::generateRandomSlime(int slimeCount) {
    for (long i = 0; i < slimeCount; i++) {
        slimeVector->push_back(Slime::generateRandom(i, &envData));
    }
}

std::string Environment::getInfoString(int spacingCount) {
    std::string spacing = std::string(spacingCount, ' ');

    std::stringstream s = std::stringstream();
    s << spacing << "Environment info:" << std::endl
      << spacing << " Width: " << envData.grid_width << std::endl
      << spacing << " Height: " << envData.grid_height << std::endl
      << spacing << " Slime count: " << getSlimeCount() << std::endl
      << spacing << " Slime list:" << std::endl << std::endl;

    for (Slime *slime: *slimeVector) {
        s << spacing << slime->getInfoString(spacingCount + 2) << std::endl;
    }

    return s.str();
}

void Environment::updateParam(InputParam &param) {
    if (param.name == "display_pheromones") {
        if (envData.display_pheromones != param.valueBool) {
            std::cout << "display_pheromones set to : [" << param.valueBool << "]" << std::endl;
            envData.display_pheromones = param.valueBool;
        }
    } else if (param.name == "display_slime") {
        if (envData.display_slime != param.valueBool) {
            std::cout << "display_slime set to : [" << param.valueBool << "]" << std::endl;
            envData.display_slime = param.valueBool;
        }
    } else if (param.name == "display_slime_size") {
        if (envData.display_slime_size != param.valueNumber) {
            std::cout << "display_slime_size set to : [" << param.valueNumber << "]" << std::endl;
            envData.display_slime_size = (int) param.valueNumber;
        }
    } else if (param.name == "display_slime_opacity") {
        if (envData.display_slime_opacity != param.valueNumber) {
            std::cout << "display_slime_opacity set to : [" << param.valueNumber << "]" << std::endl;
            envData.display_slime_opacity = (int) param.valueNumber;
        }
//    } else if (param.name == "display_slime_color") {
////        std::cout << "display_slime_color not yet implemented" << std::endl;
//    } else if (param.name == "display_highlight_pheromone_color") {
////        std::cout << "display_highlight_pheromone_color not yet implemented" << std::endl;
//    } else if (param.name == "display_inactive_pheromone_color") {
////        std::cout << "display_inactive_pheromone_color not yet implemented" << std::endl;
    } else if (param.name == "grid_width") {
        if (envData.grid_width != param.valueNumber) {
            std::cout << "grid_width set to : [" << param.valueNumber << "]" << std::endl;
            envData.grid_width = (int) param.valueNumber;
            pheromoneGrid->updateSize();
        }
    } else if (param.name == "grid_height") {
        if (envData.grid_height != param.valueNumber) {
            std::cout << "grid_height set to : [" << param.valueNumber << "]" << std::endl;
            envData.grid_height = (int) param.valueNumber;
            pheromoneGrid->updateSize();
        }
    } else if (param.name == "loop_grid") {
        if (envData.loop_grid != param.valueBool) {
            std::cout << "loop_grid set to : [" << param.valueBool << "]" << std::endl;
            envData.loop_grid = param.valueBool;
        }
    } else if (param.name == "random_natural_pheromones_count") {
        if (envData.random_natural_pheromones_count != param.valueNumber) {
            std::cout << "random_natural_pheromones_count set to : [" << param.valueNumber << "]" << std::endl;
            envData.random_natural_pheromones_count = (int) param.valueNumber;
        }
    } else if (param.name == "natural_pheromones_strength") {
        if (envData.natural_pheromones_strength != param.valueNumber) {
            std::cout << "natural_pheromones_strength set to : [" << param.valueNumber << "]" << std::endl;
            envData.natural_pheromones_strength = (int) param.valueNumber;
        }
    } else if (param.name == "slime_count") {
        if (envData.slime_count != param.valueNumber) {
            std::cout << "slime_count set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_count = (int) param.valueNumber;
        }
    } else if (param.name == "slime_speed") {
        if (envData.slime_speed != param.valueNumber) {
            std::cout << "slime_speed set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_speed = param.valueNumber;
        }
    } else if (param.name == "slime_avoid_walls") {
        if (envData.slime_avoid_walls != param.valueBool) {
            std::cout << "slime_avoid_walls set to : [" << param.valueBool << "]" << std::endl;
            envData.slime_avoid_walls = param.valueBool;
        }
    } else if (param.name == "slime_wall_detection_range") {
        if (envData.slime_wall_detection_range != param.valueNumber) {
            std::cout << "slime_wall_detection_range set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_wall_detection_range = (int) param.valueNumber;
        }
    } else if (param.name == "slime_wall_turn_angle") {
        if (envData.slime_wall_turn_angle != param.valueNumber) {
            std::cout << "slime_wall_turn_angle set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_wall_turn_angle = param.valueNumber;
        }
    } else if (param.name == "slime_seek_pheromones") {
        if (envData.slime_seek_pheromones != param.valueBool) {
            std::cout << "slime_seek_pheromones set to : [" << param.valueBool << "]" << std::endl;
            envData.slime_seek_pheromones = param.valueBool;
        }
    } else if (param.name == "slime_seek_pheromones_period") {
        if (envData.slime_seek_pheromones_period != param.valueNumber) {
            std::cout << "slime_seek_pheromones_period set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_seek_pheromones_period = (int) param.valueNumber;
        }
    } else if (param.name == "slime_pheromone_detection_range") {
        if (envData.slime_pheromone_detection_range != param.valueNumber) {
            std::cout << "slime_pheromone_detection_range set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_pheromone_detection_range = (int) param.valueNumber;
        }
    } else if (param.name == "slime_pheromone_turn_angle") {
        if (envData.slime_pheromone_turn_angle != param.valueNumber) {
            std::cout << "slime_pheromone_turn_angle set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_pheromone_turn_angle = param.valueNumber;
        }
    } else if (param.name == "slime_pheromone_level") {
        if (envData.slime_pheromone_level != param.valueNumber) {
            std::cout << "slime_pheromone_level set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_pheromone_level = (int) param.valueNumber;
        }
    } else if (param.name == "slime_ignore_self_pheromone") {
        if (envData.slime_ignore_self_pheromone != param.valueBool) {
            std::cout << "slime_ignore_self_pheromone set to : [" << param.valueBool << "]" << std::endl;
            envData.slime_ignore_self_pheromone = param.valueBool;
        }
    } else if (param.name == "slime_align_direction") {
        if (envData.slime_align_direction != param.valueBool) {
            std::cout << "slime_align_direction set to : [" << param.valueBool << "]" << std::endl;
            envData.slime_align_direction = param.valueBool;
        }
    } else if (param.name == "slime_other_detection_range") {
        if (envData.slime_other_detection_range != param.valueNumber) {
            std::cout << "slime_other_detection_range set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_other_detection_range = (int) param.valueNumber;
        }
    } else if (param.name == "slime_align_turn_angle") {
        if (envData.slime_align_turn_angle != param.valueNumber) {
            std::cout << "slime_align_turn_angle set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_align_turn_angle = param.valueNumber;
        }
    } else if (param.name == "slime_random_rotation_chance") {
        if (envData.slime_random_rotation_chance != param.valueNumber) {
            std::cout << "slime_random_rotation_chance set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_random_rotation_chance = param.valueNumber;
        }
    } else if (param.name == "slime_random_rotation_angle") {
        if (envData.slime_random_rotation_angle != param.valueNumber) {
            std::cout << "slime_random_rotation_angle set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_random_rotation_angle = param.valueNumber;
        }
    } else if (param.name == "slime_bias_direction") {
        if (envData.slime_bias_direction != param.valueBool) {
            std::cout << "slime_bias_direction set to : [" << param.valueBool << "]" << std::endl;
            envData.slime_bias_direction = param.valueBool;
        }
    } else if (param.name == "slime_bias_direction_x") {
        if (envData.slime_bias_direction_x != param.valueNumber) {
            std::cout << "slime_bias_direction_x set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_bias_direction_x = (int) param.valueNumber;
        }
    } else if (param.name == "slime_bias_direction_y") {
        if (envData.slime_bias_direction_y != param.valueNumber) {
            std::cout << "slime_bias_direction_y set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_bias_direction_y = (int) param.valueNumber;
        }
    } else if (param.name == "slime_bias_rotation_angle") {
        if (envData.slime_bias_rotation_angle != param.valueNumber) {
            std::cout << "slime_bias_rotation_angle set to : [" << param.valueNumber << "]" << std::endl;
            envData.slime_bias_rotation_angle = param.valueNumber;
        }
    } else if (param.name == "pheromone_max_level") {
        if (envData.pheromone_max_level != param.valueNumber) {
            std::cout << "pheromone_max_level set to : [" << param.valueNumber << "]" << std::endl;
            envData.pheromone_max_level = (int) param.valueNumber;
        }
    } else if (param.name == "pheromone_high_level_diffusion_multiplier") {
        if (envData.pheromone_high_level_diffusion_multiplier != param.valueNumber) {
            std::cout << "pheromone_high_level_diffusion_multiplier set to : [" << param.valueNumber << "]"
                      << std::endl;
            envData.pheromone_high_level_diffusion_multiplier = param.valueNumber;
        }
    } else if (param.name == "pheromone_low_level_diffusion_multiplier") {
        if (envData.pheromone_low_level_diffusion_multiplier != param.valueNumber) {
            std::cout << "pheromone_low_level_diffusion_multiplier set to : [" << param.valueNumber << "]" << std::endl;
            envData.pheromone_low_level_diffusion_multiplier = (int) param.valueNumber;
        }
    } else if (param.name == "pheromone_diffusion_constant") {
        if (envData.pheromone_diffusion_constant != param.valueNumber) {
            std::cout << "pheromone_diffusion_constant set to : [" << param.valueNumber << "]" << std::endl;
            envData.pheromone_diffusion_constant = (int) param.valueNumber;
        }
    } else if (param.name == "pheromone_max_level_reset_value") {
        if (envData.pheromone_max_level_reset_value != param.valueNumber) {
            std::cout << "pheromone_max_level_reset_value set to : [" << param.valueNumber << "]" << std::endl;
            envData.pheromone_max_level_reset_value = (int) param.valueNumber;
        }
    } else {
        std::cout << "UNRECOGNIZED PARAMETER: [" << param.name << "]" << std::endl;
    }
}

void Environment::updateParameters() {
    std::string paramFileName = PARAMETER_FILE_NAME;
    std::vector<InputParam> params = ParameterReader::read(paramFileName);
    for (auto & param : params) {
        updateParam(param);
    }
}

EnvironmentData *Environment::getEnvironmentData() {
    return &envData;
}
