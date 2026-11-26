#include "two_fer.h"
void two_fer(char *buffer, const char *name){
    const char *recipient = (name != NULL && name[0] != '\0') ? name : "you";
    sprintf(buffer, "One for %s, one for me.", recipient);
}