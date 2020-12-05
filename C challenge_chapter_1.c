#include <stdio.h>
#include <math.h>

int main()
{
    float a, b, p, sa, sb;

    scanf("%f", &a);
    scanf("%f", &b);
    p = pow(a,b);
    sa = sqrt(a);
    sb = sqrt(b);
    printf("The results are:\n"
           "a + b = %f,\n"
           "a - b = %f,\n"
           "a^b = %f,\n"
           "sqrt(a) = %f,\n"
           "sqrt(b) = %f\n", a+b, a-b, p, sa, sb);

    return(0);
}
