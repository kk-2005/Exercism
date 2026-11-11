#include "hamming.h"
#include <stddef.h>

int compute(const char *lhs, const char *rhs) {
    if (!lhs || !rhs) {
        return -1;
    }

    int distance = 0;
    int i = 0;

    while (lhs[i] != '\0' && rhs[i] != '\0') {
        if (lhs[i] != rhs[i]) {
            distance++;
        }
        i++;
    }
    // Return -1 if one string is longer than the other
    if (lhs[i] != rhs[i]) {
        return -1;
    }

    return distance;
}