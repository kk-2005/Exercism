#ifndef DARTS_H
#define DARTS_H
#include <stdio.h>
typedef struct {
    double x;
    double y;
} coordinate_t;

int score(coordinate_t landing_position);
#endif
