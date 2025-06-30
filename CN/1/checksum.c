#include <stdio.h>
#include <string.h>
#define N 20
void binaryAddition(char a[], char b[], char sum[])
{
    int carry = 0, i;
    int len = strlen(a);
    for (i = len - 1; i >= 0; i--)
    {
        int bitA = a[i] - '0';
        int bitB = b[i] - '0';
        int bitSum = bitA + bitB + carry;
        sum[i] = (bitSum % 2) + '0';
        carry = bitSum / 2;
    }
    if (carry)
    {
        for (i = len - 1; i >= 0; i--)
        {
            int bitSum = (sum[i] - '0') + carry;
            sum[i] = (bitSum % 2) + '0';
            carry = bitSum / 2;
        }
    }
    sum[len] = '\0';
}

void onesComplement(char sum[], char complement[])
{
    int len = strlen(sum);
    int i;
    for (i = 0; i < len; i++)
    {
        complement[i] = (sum[i] == '0') ? '1' : '0';
    }
    complement[len] = '\0';
}

int isAllOnes(char str[])
{
    int i;
    for (i = 0; i < strlen(str); i++)
    {
        if (str[i] != '1')
            return 0;
    }
    return 1;
}

int main()
{
    int choice;
    char firstBin[N], secondBin[N], checksum[N], receivedChecksum[N], sum[N];
    while (1)
    {
        printf("\nChecksum Menu:\n1. Transmitter\n2. Receiver\n3. Exit\nEnter your choice: ");
        scanf("%d", &choice);

        if (choice == 1)
        {
            printf("Enter the first binary number: ");
            scanf("%s", firstBin);
            printf("Enter the second binary number: ");
            scanf("%s", secondBin);
            binaryAddition(firstBin, secondBin, sum);
            onesComplement(sum, checksum);
            printf("The sum of the two binary numbers is: %s\n", sum);
            printf("Complement of the sum is: %s\n", checksum);
            printf("Encoded data: %s %s %s\n", firstBin, secondBin, checksum);
        }
        else if (choice == 2)
        {
            printf("Enter the first binary number: ");
            scanf("%s", firstBin);
            printf("Enter the second binary number: ");
            scanf("%s", secondBin);
            printf("Enter the checksum values: ");
            scanf("%s", receivedChecksum);
            binaryAddition(firstBin, secondBin, sum);
            binaryAddition(sum, receivedChecksum, sum);
            if (isAllOnes(sum))
            {
                printf("There is no error in the received data.\n");
                printf("Decoded data: %s %s\n", firstBin, secondBin);
            }
            else
            {
                printf("Error detected in the received data!\n");
            }
        }
        else if (choice == 3)
        {
            break;
        }
        else
        {
            printf("Invalid choice! Please enter 1, 2, or 3.\n");
        }
    }
    return 0;
}
