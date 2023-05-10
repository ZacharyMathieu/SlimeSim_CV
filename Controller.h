//
// Created by zwazo on 2022-09-24.
//

#ifndef SLIMESIMAPP_WINDOWINTERFACE_H
#define SLIMESIMAPP_WINDOWINTERFACE_H

#include "Environment.h"
#include "UI/Widget.h"

class Controller {
public:
    explicit Controller(Environment *e);

    explicit Controller(Widget *w, Environment *e);

    void displayEnvironment();

    void physics();

    void animate();
    void updateParameters();
private:
    Environment *env;
    Widget *widget;
    //    QColor* backgroud;
};


#endif //SLIMESIMAPP_WINDOWINTERFACE_H
