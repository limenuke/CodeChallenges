#include<stdio.h>
#define MAX 50


int main (int argc,  char * argv[]) {

    int size = argc;
    int * arr = (int*)malloc(sizeof(int)*size));
    
    for (int i = 0; i < size; i++){
        arr[i]=argv[i+2];
    }
    
    int mid = size/2;
   
    partition(arr,0,size-1);
}

void partition(arr,low,high){

    if (low<high) {
        int mid = (high-low)/2;
        partition(arr,low,mid);
        partition(arr,mid+1,high);
        merge(arr,low,mid,high);
        return;
    }
    else {
        return;
    }
    
}


void merge(arr,low,mid,high) {
    int tempsize = high-low+1;
    int * temp = (int*)malloc(sizeof(int)*(tempsize));
    int i=0,j=mid+1,k=0;
    while (i<=mid && j<=high &&) {
        if (arr[i] < arr[j]) {
            temp[k]=arr[i];
            i++;
        }
        else {
            temp[k]=arr[j];
            j++;
        }
        k++;
    }
    
    
    
    }
    



}