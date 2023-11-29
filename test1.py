#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int num;
    FILE* fp = fopen("num.bin", "wb");
    for (num = 1; num < 101; num++) {
        fwrite(&num, sizeof(int), 1, fp);
    }
    fclose(fp);
    fp = fopen("num.bin", "rb");
    for (num = 1; num < 101; num++) {
        fread(&num, sizeof(int), 1, fp);
        printf("%d\n", num);
    }
    fclose(fp);
}
