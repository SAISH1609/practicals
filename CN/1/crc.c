#include <stdio.h>
#include <string.h>
#define N 100

void xorOperation(char dividend[], char divisor[], int start){
	int i;
    for (i = 0; i < strlen(divisor); i++) {
        dividend[start + i] = (dividend[start + i] == divisor[i]) ? '0' : '1';
    }
}
void crcDivision(char data[], char generator[], char remainder[]){
    int dataLen = strlen(data);
    int i;
    int genLen = strlen(generator);
    char temp[N];
    strcpy(temp, data);
    for (i = 0; i <= dataLen - genLen; i++) {
        if (temp[i] == '1') {
            xorOperation(temp, generator, i);
        }
    }
    strncpy(remainder, temp + dataLen - genLen + 1, genLen - 1);
    remainder[genLen - 1] = '\0';
}

void appendCRC(char data[], char generator[], char finalData[]) {
    int dataLen = strlen(data);
    int i;
    int genLen = strlen(generator);    
    char paddedData[N];
    strcpy(paddedData, data);
    for (i = 0; i < genLen - 1; i++) {
        strcat(paddedData, "0");
    }
    char remainder[N];
    printf("Data padded with n-1 zeros: %s\n", paddedData);
    crcDivision(paddedData, generator, remainder);    
    strcpy(finalData, data);
    strcat(finalData, remainder);
}

int main(){
    int choice;
    char data[N], generator[N], receivedData[N];
    while (1) {
        printf("\nMenu\n1. Transmitter\n2. Receiver\n3. Exit\nEnter your Choice: ");
        scanf("%d", &choice);
        if (choice == 1) {
            printf("Enter data to be transmitted: ");
            scanf("%s", data);
            printf("Enter the Generating polynomial: ");
            scanf("%s", generator);
            char finalData[N];
            appendCRC(data, generator, finalData);
            printf("CRC or Check value is: %s\n", finalData + strlen(data));
            printf("Final data to be sent: %s\n", finalData);
        } 
        else if (choice == 2) {
            printf("Enter the received data: ");
            scanf("%s", receivedData);
            printf("Enter the Generating polynomial: ");
            scanf("%s", generator);
            char remainder[N];
            crcDivision(receivedData, generator, remainder);
            if (strchr(remainder, '1') == NULL) {
                printf("No error detected.\n");
                printf("Data sent is %.*s\n", (int)(strlen(receivedData) - strlen(generator) + 1), receivedData);
            } else {
                printf("Error detected.\n");
            }
        } 
        else if (choice == 3) {
            break;
        } 
        else {
            printf("Invalid choice! Please enter 1, 2, or 3.\n");
        }
    }

    return 0;
}
