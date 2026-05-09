#include <stdio.h>

int main() {
    int scores[5] = {85, 92, 78, 90, 88};
    int total_score = 0;
    int num_elements = 5;

    printf("Displaying Scores:\n");

    // DÜZƏLİŞ: i < num_elements (yəni i maksimum 4 ola bilər)
    for (int i = 0; i < num_elements; i++) {
        printf("Score %d: %d\n", i + 1, scores[i]);
        total_score += scores[i];
    }

    float average = (float)total_score / num_elements;
    printf("\nTotal: %d", total_score);
    printf("\nAverage Score: %.2f\n", average);

    return 0;
}
