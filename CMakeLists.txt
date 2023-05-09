cmake_minimum_required(VERSION 3.23)
project(SlimeSim_CV)

set(CMAKE_CXX_STANDARD 14)

include_directories(opencv2/include)
find_package(OpenCV REQUIRED)
#include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(CV_SlimeSim
        main.cpp
        EnvironmentData.h
        Environment.h
        Environment.cpp
        Slime.h
        Slime.cpp
        Random.h
        Pheromone.h
        Pheromone.cpp
        PheromoneGrid.h
        PheromoneGrid.cpp
        ParameterReader.h
        ParameterReader.cpp
        Constants.h)
