//
// Created by zwazo on 2022-09-24.
//

#ifndef SLIMESIM_SLIME_H
#define SLIMESIM_SLIME_H

#include "EnvironmentData.h"
#include "PheromoneGrid.h"

#include <string>

class Slime {
private :
    double x, y, angle;
    long id;

    Slime *lastSlimeAligned;

    EnvironmentData *envData;

    void turn(bool canBeRandom, double angle);

    void turnToAngle(bool canBeRandom, double angle, double maxTurnAngle);

    void turnTorwards(int targetX, int targetY, double angle);

    bool seekPheromones(PheromoneGrid *grid);

    bool avoidWalls(double xSpeed, double ySpeed);

    bool alignDirectionWithNearbySlime(std::vector<Slime*> *slimes);

    void alignDirectionWithSlime(Slime *slime);
public:
    Slime(long _id, EnvironmentData *data);

    double getX() const;

    double getY() const;

    long getId() const;

    static Slime *generateRandom(long _id, EnvironmentData *data);

    void setRandomValues();

    void moveForward(PheromoneGrid* grid, std::vector<Slime*> *slimes, bool _seekPheromones);

    std::string getInfoString(int spacingCount) const;
};

#endif //SLIMESIM_SLIME_H
