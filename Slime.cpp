//
// Created by zwazo on 2022-09-24.
//
#include <iostream>
#include <sstream>
#include <cmath>

#include "Slime.h"
#include "Random.h"

Slime::Slime(long _id, EnvironmentData *data) {
    id = _id;

    envData = data;

    x = 0;
    y = 0;
    angle = 0;

    lastSlimeAligned = nullptr;
}

double Slime::getX() const { return x; }

double Slime::getY() const { return y; }

long Slime::getId() const { return id; }

Slime *Slime::generateRandom(long _id, EnvironmentData *data) {
    Slime *s = new Slime(_id, data);
    s->setRandomValues();
    return s;
}

void Slime::setRandomValues() {
    x = Random::getRandomDouble() * (envData->grid_width - 1);
    y = Random::getRandomDouble() * (envData->grid_height - 1);
    angle = Random::getRandomDouble() * (2 * M_PI);
}

void Slime::moveForward(PheromoneGrid* grid, std::vector<Slime*> *slimes, bool _seekPheromones) {
    double xSpeed = envData->slime_speed * cos(angle);
    double ySpeed = envData->slime_speed * sin(angle);

    x += xSpeed;
    y += ySpeed;

    if (x < 0) {
        if (envData->loop_grid) {
            x += envData->grid_width;
        } else {
            x = 0;
        }
    } else if (x >= envData->grid_width) {
        if (envData->loop_grid) {
            x -= envData->grid_width;
        } else {
            x = envData->grid_width - 1;
        }
    }

    if (y < 0) {
        if (envData->loop_grid) {
            y += envData->grid_height;
        } else {
            y = 0;
        }
    } else if (y >= envData->grid_height) {
        if (envData->loop_grid) {
            y -= envData->grid_height;
        } else {
            y = envData->grid_height - 1;
        }
    }

    if (envData->slime_avoid_walls) {
        avoidWalls(xSpeed, ySpeed);
    }

    {
        bool decisionDone = false;

        if (envData->slime_seek_pheromones) {
            if (_seekPheromones) {
                decisionDone = seekPheromones(grid);
            }
        }

//        if (!decisionDone) {
            if (envData->slime_align_direction) {
                decisionDone = alignDirectionWithNearbySlime(slimes);
            }
//        }

//        if (!decisionDone) {
            if (envData->slime_bias_direction) {
                turnTorwards(envData->slime_bias_direction_x, envData->slime_bias_direction_y, envData->slime_bias_rotation_angle);
            }
//        }
    }
}

bool Slime::avoidWalls(double xSpeed, double ySpeed) {
    bool madeTurn = false;

    if (x < envData->slime_wall_detection_range) {
        madeTurn = true;
        if (ySpeed >= 0) turn(false, -envData->slime_wall_turn_angle);
        else turn(false, envData->slime_wall_turn_angle);
    } else if (x > envData->grid_width - envData->slime_wall_detection_range) {
        madeTurn = true;
        if (ySpeed >= 0) turn(false, envData->slime_wall_turn_angle);
        else turn(false, -envData->slime_wall_turn_angle);
    } else if (y < envData->slime_wall_detection_range) {
        madeTurn = true;
        if (xSpeed >= 0) turn(false, envData->slime_wall_turn_angle);
        else turn(false, -envData->slime_wall_turn_angle);
    } else if (y > envData->grid_height - envData->slime_wall_detection_range) {
        madeTurn = true;
        if (xSpeed >= 0) turn(false, -envData->slime_wall_turn_angle);
        else turn(false, envData->slime_wall_turn_angle);
    }

    return madeTurn;
}

bool Slime::seekPheromones(PheromoneGrid *pheromoneGrid) {
    int roundedX = round(x);
    int minX = std::max(roundedX - envData->slime_pheromone_detection_range, 0);
    int maxX = std::min(roundedX + envData->slime_pheromone_detection_range, envData->grid_width - 1);

    int roundedY = floor(y);
    int minY = std::max(roundedY - envData->slime_pheromone_detection_range, 0);
    int maxY = std::min(roundedY + envData->slime_pheromone_detection_range, envData->grid_height - 1);

    if (M_PI / 4 <= angle && angle < 3 * M_PI / 4) {
        minY = roundedY;
    } else if (3 * M_PI / 4 <= angle && angle < 5 * M_PI / 4) {
        maxX = roundedX;
    } else if (5 * M_PI / 4 <= angle && angle < 7 * M_PI / 4) {
        maxY = roundedY;
    } else {
        minX = roundedX;
    }

    auto grid = pheromoneGrid->getGrid();

    bool pheromoneFound = false;
    std::pair<int, int> strongestPheromonePos;
    double strongestPheromoneDistance;
    int strongestPheromone = 0;
    for (int iY = minY; iY < maxY; iY++) {
        for (int iX = minX; iX < maxX; iX++) {
            Pheromone *p = grid->at(iY).at(iX);

            if (p->level >= strongestPheromone) {
                if (!envData->slime_ignore_self_pheromone || p->slimeId != id) {
                    if (pheromoneFound && p->level == strongestPheromone) {
                        double newDistance = sqrt(pow(iX - x, 2) + pow(iY - y, 2));
                        if (strongestPheromoneDistance < newDistance) {
                            strongestPheromonePos = std::make_pair(iX, iY);
                            strongestPheromoneDistance = newDistance;
                        }
                    } else {
                        pheromoneFound = true;
                        strongestPheromone = p->level;
                        strongestPheromonePos = std::make_pair(iX, iY);
                        strongestPheromoneDistance = sqrt(pow(strongestPheromonePos.first - x, 2) + pow(strongestPheromonePos.second - y, 2));
                    }
                }
            }
        }
        if (pheromoneFound && strongestPheromone == envData->pheromone_max_level) break;
    }

    if (pheromoneFound) {
        turnTorwards(strongestPheromonePos.first, strongestPheromonePos.second, envData->slime_pheromone_turn_angle);
    }

    return pheromoneFound;
}

void Slime::turn(bool canBeRandom, double turnAngle) {
    if (canBeRandom && Random::getRandomBool(envData->slime_random_rotation_chance)) {
        if (Random::getRandomBool(0.5)) angle += envData->slime_random_rotation_chance;
        else angle -= envData->slime_random_rotation_chance;
    } else angle += turnAngle;

    if (2 * M_PI < angle){
        angle -= 2 * M_PI;
    } else if (angle < 0) {
        angle += 2 * M_PI;
    }
}

void Slime::turnToAngle(bool canBeRandom, double targetAngle, double maxTurnAngle) {
    if (targetAngle < angle) targetAngle += 2 * M_PI;

    if (std::abs(targetAngle - angle) > std::abs(targetAngle - (angle + (2 * M_PI))))
        targetAngle -= 2 * M_PI;

    double angleDiff = std::abs(angle - targetAngle);

    double turnAngle = std::min(maxTurnAngle, angleDiff);

    if (targetAngle > angle) turnAngle = turnAngle;
    else turnAngle = -turnAngle;

    turn(canBeRandom, turnAngle);
}

void Slime::turnTorwards(int targetX, int targetY, double maxAngle) {
    int floorX = floor(x);
    int floorY = floor(y);

    double centeredX = targetX - floorX;
    double centeredY = targetY - floorY;

    double targetAngle = atan(centeredY / centeredX);

    if (centeredX < 0) targetAngle += M_PI;

    if (targetAngle < 0) targetAngle += 2 * M_PI;

    turnToAngle(true, targetAngle, maxAngle);
}

bool Slime::alignDirectionWithNearbySlime(std::vector<Slime*> *slimes) {
    bool slimeFound = false;

    if (!slimeFound) {
        for (Slime* pS : *slimes) {
            double dX = std::abs(x - pS->getX());
            double dY = std::abs(y - pS->getY());

            if (dX < envData->slime_other_detection_range && dY < envData->slime_other_detection_range) {
                if (sqrt((dX * dX) + (dY * dY)) <= envData->slime_other_detection_range) {
                    if (pS != this) {
                        slimeFound = true;
                        lastSlimeAligned = pS;
                        alignDirectionWithSlime(pS);
                        break;
                    }
                }
            }
        }
    }

    if (!slimeFound) {
        lastSlimeAligned = nullptr;
    }

    return slimeFound;
}

void Slime::alignDirectionWithSlime(Slime *slime) {
    turnToAngle(true, slime->angle, envData->slime_align_turn_angle);
}

std::string Slime::getInfoString(int spacingCount) const {
    std::string spacing = std::string(spacingCount, ' ');

    std::stringstream s = std::stringstream();
    s << spacing << "Slime info:" << std::endl
      << spacing << " X: " << x << std::endl
      << spacing << " Y: " << y << std::endl
      << spacing << " Angle: " << angle << std::endl
      << spacing << " Speed: " << envData->slime_speed << std::endl;

    return s.str();
}
