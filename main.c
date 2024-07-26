#include <stdio.h>
#include <math.h>

int main(int argc, char ** argv){
    //TERNARY OPERATOR
    //expression ? true : false
    // if(expression){
    //     true;
    // }
    // else{
    //     false;
    // }
    float affec = 17.38;
    int AffecLevel;

    affec == 100.0 ? AffecLevel = 5 : (AffecLevel = ceil(affec/25));
    printf("%d\n", AffecLevel);
    
    return 0;
}