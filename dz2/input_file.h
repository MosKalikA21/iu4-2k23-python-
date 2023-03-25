#ifndef EXAMPLE_H
#define EXAMPLE_H

#include <stdio.h>

typedef struct {
    int x;
    int y;
} Point;

int sum(int a, int b);

double average(double* array, int size);

inline int max(int a, int b) {
    int result = a > b ? a : b;
    return result;
}

#endif
