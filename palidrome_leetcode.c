#include<stdio.h>
int main()
{
int n = -212;
int sum,r;
int temp = n;
while(n>0){
     r = n%10;
     sum = (sum*10)+r;
     n = n/10;
}
printf("%d ",temp);
if (temp==sum)
{
    printf("yo");
}

return 0;
}