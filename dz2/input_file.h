#ifndef EXAMPLE_H
#define EXAMPLE_H

#include <stdio.h>

typedef struct {
    int x;
    int y;
} Point;

int sum(int a1, int b1);

double average(double* array, int size);

inline int max(int a1, int b1) {
    int result = a1 > b1 ? a1 : b1;
    return result;
}

#endif
