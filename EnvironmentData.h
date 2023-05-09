//
// Created by zwazo on 2022-09-24.
//

#ifndef SLIMESIM_ENVIRONMENTDATA_H
#define SLIMESIM_ENVIRONMENTDATA_H

#include "Constants.h"

#include <vector>
#include <tuple>

struct EnvironmentData {
    bool display_pheromones = DISPLAY_PHEROMONES;
    bool display_slime = DISPLAY_SLIME;
    int display_slime_size = DISPLAY_SLIME_SIZE;
    int display_slime_opacity = DISPLAY_SLIME_OPACITY;
    int display_slime_color[4] = DISPLAY_SLIME_COLOR;
    int display_highlight_pheromone_color[4] = DISPLAY_HIGHLIGHT_PHEROMONE_COLOR;
    int display_inactive_pheromone_color[4] = DISPLAY_INACTIVE_PHEROMONE_COLOR;
    int grid_width = GRID_WIDTH;
    int grid_height = GRID_HEIGHT;
    bool loop_grid = LOOP_GRID;
    int random_natural_pheromones_count = RANDOM_NATURAL_PHEROMONES_COUNT;
    int natural_pheromones_strength = NATURAL_PHEROMONES_STRENGTH;
    int slime_count = SLIME_COUNT;
    bool slime_avoid_walls = SLIME_AVOID_WALLS;
    double slime_speed = SLIME_SPEED;
    int slime_wall_detection_range = SLIME_WALL_DETECTION_RANGE;
    double slime_wall_turn_angle = SLIME_WALL_TURN_ANGLE;
    bool slime_seek_pheromones = SLIME_SEEK_PHEROMONES_PERIOD;
    int slime_seek_pheromones_period = SLIME_SEEK_PHEROMONES_PERIOD;
    int slime_pheromone_detection_range = SLIME_PHEROMONE_DETECTION_RANGE;
    double slime_pheromone_turn_angle = SLIME_PHEROMONE_TURN_ANGLE;
    int slime_pheromone_level = SLIME_PHEROMONE_LEVEL;
    bool slime_ignore_self_pheromone = SLIME_IGNORE_SELF_PHEROMONE;
    bool slime_align_direction = SLIME_ALIGN_DIRECTION;
    int slime_other_detection_range = SLIME_OTHER_DETECTION_RANGE;
    double slime_align_turn_angle = SLIME_ALIGN_TURN_ANGLE;
    double slime_random_rotation_chance = SLIME_RANDOM_ROTATION_CHANCE;
    double slime_random_rotation_angle = SLIME_RANDOM_ROTATION_ANGLE;
    bool slime_bias_direction = SLIME_BIAS_DIRECTION;
    int slime_bias_direction_x = SLIME_BIAS_DIRECTION_X;
    int slime_bias_direction_y = SLIME_BIAS_DIRECTION_Y;
    double slime_bias_rotation_angle = SLIME_BIAS_ROTATION_ANGLE;
    int pheromone_max_level = PHEROMONE_MAX_LEVEL;
    double pheromone_high_level_diffusion_multiplier = PHEROMONE_HIGH_LEVEL_DIFFUSION_MULTIPLIER;
    int pheromone_low_level_diffusion_multiplier = PHEROMONE_LOW_LEVEL_DIFFUSION_MULTIPLIER;
    int pheromone_diffusion_constant = PHEROMONE_DIFFUSION_CONSTANT;
    int pheromone_max_level_reset_value = PHEROMONE_MAX_LEVEL_RESET_VALUE;
};

#endif //SLIMESIM_ENVIRONMENTDATA_H
