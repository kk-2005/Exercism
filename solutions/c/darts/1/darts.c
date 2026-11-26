#include "darts.h"
int score(coordinate_t landing_position) {
    double dist_sq = (landing_position.x * landing_position.x) +
                     (landing_position.y * landing_position.y);

    if (dist_sq <= 1.0) {
        return 10;
    }
    if (dist_sq <= 25.0) {
        return 5;
    }
    if (dist_sq <= 100.0) {
        return 1;
    }
    return 0;
}