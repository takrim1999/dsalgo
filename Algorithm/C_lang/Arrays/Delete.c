#include<stdio.h>
int main(){
    int new=0,temp=0,array[8]={1,2,3,4,5,6,7};
    for(int i=0;i<=7;i++){
        printf("%d",array[i]);
    }
    printf("\n");
    printf("Index of element you want to delete?\n>");
    scanf("%d",&new);
    // printf("%d\n",new);
    
    for(int i=7;i>=new;i--){
       array[i] = temp;
       temp = array[i-1];
       array[i-1] = array[i];
    }
    
    for(int i=0;i<=7;i++){
        printf("%d",array[i]);
    }
    printf("\n");

    return 0;
}