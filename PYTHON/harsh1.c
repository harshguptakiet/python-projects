#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int arr[5] = {1, 2, 3, 5, 67};
    int n;
    
    // Read the index from the user
    scanf("%d", &n);
    
    // Check if the index is within bounds
    if (n >= 0 && n < 5) {
        printf("%d", arr[n]);
    } else {
        printf("Index out of bounds");
    }

    return 0;
}
