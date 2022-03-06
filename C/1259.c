#include <stdio.h>
#include <stdlib.h>

int pontPAR(void const *a, void const *b ){
    return (*(int*)a - *(int*)b );
}
int pontIMP(void const *a, void const *b ){
    return (*(int*)b - *(int*)a );
}
int main(){
    int n, i, num, par, impar;
    scanf("%d", &n);
    par = 0;
    impar = 0;
    int numpar[n];
    int numimp[n];

    for(i = 0; i < n; i++){
        scanf("%d", &num);
        if(num%2 == 0){
            numpar[par] = num;
            par++;
        }

        else{
            numimp[impar] = num;
            impar++;
        }
    }
    qsort(numpar, par, sizeof(int), pontPAR);
    qsort(numimp, impar, sizeof(int), pontIMP);

    for(i = 0; i < par; i++){
        printf("%d\n",numpar[i]);
    }
    for(i = 0; i < impar; i++){
        printf("%d\n",numimp[i]);
    }
    return 0;
}