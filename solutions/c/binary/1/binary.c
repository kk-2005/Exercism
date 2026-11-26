#include "binary.h"
int convert(const char *input){
    int decimal=0;
    for(int i=0;input[i]!='\0';i++){
        if (input[i]=='1'){
            decimal=2*decimal+1;
        }
        else if (input[i]=='0'){
            decimal=2*decimal;
        }
        else{
            return -1;
        }
    }
    return decimal;
}