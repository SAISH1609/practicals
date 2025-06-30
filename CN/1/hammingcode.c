#include <stdio.h>
#include <math.h>
void generateHammingCode(int dataBits[], int encodedBits[]) {
    encodedBits[2] = dataBits[0]; 
    encodedBits[4] = dataBits[1]; 
    encodedBits[5] = dataBits[2]; 
    encodedBits[6] = dataBits[3]; 
    encodedBits[0] = encodedBits[2] ^ encodedBits[5]; 
    encodedBits[1] = encodedBits[4] ^ encodedBits[5]; 
    encodedBits[3] = encodedBits[4]; 
}
int detectAndCorrectError(int receivedBits[]){
    int p1 = receivedBits[0] ^ receivedBits[2] ^ receivedBits[5];
    int p2 = receivedBits[1] ^ receivedBits[4] ^ receivedBits[5];
    int p3 = receivedBits[3] ^ receivedBits[4];
	int i;
    int errorPosition = p1 * 1 + p2 * 2 + p3 * 4; 
    //printf("Error detected at position: %d\n", errorPosition);
    if (errorPosition != 0){
        receivedBits[errorPosition - 1] ^= 1; 
        printf("Error corrected at position: %d.\n", errorPosition);
    } else{
        printf("No error detected in transmission.\n");
    }
    return errorPosition;
}
int main(){
    int dataBits[4], encodedBits[7], receivedBits[7],i;
    printf("Enter 4 bits of data one by one: \n");
    for (i = 0; i < 4; i++) {
        scanf("%d", &dataBits[i]);
    }
    generateHammingCode(dataBits, encodedBits);
    printf("Encoded data is: ");
    for (i = 0; i < 7; i++) {
        printf("%d", encodedBits[i]);
    }
    printf("\n");
    printf("Enter received data bits one by one: \n");
    for (i = 0; i < 7; i++) {
        scanf("%d", &receivedBits[i]);
    }
    int errorPosition = detectAndCorrectError(receivedBits);
    printf("Final received data after correction: ");
    for (i = 0; i < 7; i++) {
        printf("%d", receivedBits[i]);
    }
    printf("\n");
    return 0;
}

