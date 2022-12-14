#include<stdio.h>

int main()
{
    int arr[5] = {2,3,4,6,1};
    int res[2] ={};
    int target;
    scanf("%d",&target);
    int i,j;
    for ( i = 0; i < 5-1; i++)
    {
        for ( j = i+1; j < 5; j++)
        {
            if ((arr[i]+arr[j])==target)
            {
              
                res[0] = i;
                res[1] = j;
                break;
            }
            
        }
        
    }
    printf("%d %d ",res[0],res[1]);
    
    return 0;
}