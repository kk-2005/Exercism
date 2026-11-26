#include "eliuds_eggs.h"
int egg_count(int value){
    int count=0;
    for(int i=value;i!=0;i/=2){
        if (i%2==1) count++;
    }
    return count;
}