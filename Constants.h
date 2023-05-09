#ifndef CONSTANTS_H
#define CONSTANTS_H

// TODO fix memory leak

// Window settings
#define WINDOW_WIDTH                                1600
#define WINDOW_HEIGHT                               800

// Display settings
#define DISPLAY_PHEROMONES                          true
#define DISPLAY_SLIME                               true
#define DISPLAY_SLIME_SIZE                          1
#define DISPLAY_SLIME_OPACITY                       75
#define DISPLAY_SLIME_COLOR                         {255, 255, 0, DISPLAY_SLIME_OPACITY}
#define DISPLAY_HIGHLIGHT_PHEROMONE_COLOR           {0, 255, 0, 255}
#define DISPLAY_INACTIVE_PHEROMONE_COLOR            {255, 0, 255, 255}
#define DISPLAY_DEFAULT_PHEROMONE_COLOR(level)      QColor(0, std::min((1 - level) * 2, 1.0) * level * 255, level * 255)
#define COLOR_FROM_ARRAY(t)                         QColor(t[0], t[1], t[2], t[3])

// Grid settings
#define GRID_WIDTH                                  400
#define GRID_HEIGHT                                 200
#define LOOP_GRID                                   true

// Natural pheromones settings
#define RANDOM_NATURAL_PHEROMONES_COUNT             0
#define NATURAL_PHEROMONES_STRENGTH                 PHEROMONE_MAX_LEVEL

// Environment settings
#define SLIME_COUNT                                 10000

// Slime general settings
#define SLIME_SPEED                                 0.5

// Slime wall avoidance settings
#define SLIME_AVOID_WALLS                           true
#define SLIME_WALL_DETECTION_RANGE                  10
#define SLIME_WALL_TURN_ANGLE                       0.05

// Slime pheromones settings
#define SLIME_SEEK_PHEROMONES                       true
#define SLIME_SEEK_PHEROMONES_PERIOD                2
#define SLIME_PHEROMONE_DETECTION_RANGE             5
#define SLIME_PHEROMONE_TURN_ANGLE                  0.5
#define SLIME_PHEROMONE_LEVEL                       25
#define SLIME_IGNORE_SELF_PHEROMONE                 true

// Slime direction alignment settings
#define SLIME_ALIGN_DIRECTION                       false
#define SLIME_OTHER_DETECTION_RANGE                 SLIME_PHEROMONE_DETECTION_RANGE
#define SLIME_ALIGN_TURN_ANGLE                      0.1

// Slime random rotation settings
#define SLIME_RANDOM_ROTATION_CHANCE                0.1
#define SLIME_RANDOM_ROTATION_ANGLE                 1

// Slime default direction settings
#define SLIME_BIAS_DIRECTION                        true
#define SLIME_BIAS_DIRECTION_X                      (GRID_WIDTH / 2)
#define SLIME_BIAS_DIRECTION_Y                      (GRID_HEIGHT / 2)
#define SLIME_BIAS_ROTATION_ANGLE                   0.01

// Pheromones settings
#define PHEROMONE_MAX_LEVEL                         1000
#define PHEROMONE_HIGH_LEVEL_DIFFUSION_MULTIPLIER   0.5
#define PHEROMONE_LOW_LEVEL_DIFFUSION_MULTIPLIER    0
#define PHEROMONE_DIFFUSION_CONSTANT                5
#define PHEROMONE_MAX_LEVEL_RESET_VALUE             PHEROMONE_MAX_LEVEL

// Parameters settings
#define PARAMETER_FILE_NAME                         "parameters.txt"
#define PARAMETER_DELIMITER                         ' '

#endif // CONSTANTS_H
