//
// Created by zwazo on 2022-09-24.
//

#include "Controller.h"

#include <QPainter>
#include <iostream>

Controller::Controller(Environment *e) {
    env = e;
}

Controller::Controller(Widget* w, Environment *e) : Controller(e) {
    widget = w;
}

void Controller::physics() {
    env->physics();
}

void Controller::animate() {
    physics();
    widget->update();
}

void Controller::updateParameters() {
    env->updateParameters();
}
