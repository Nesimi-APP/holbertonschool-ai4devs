#include <stdio.h>

int main() {
    // 5 elementli tam ədəd massivi
    int scores[5] = {85, 92, 78, 90, 88};
    int total_score = 0;
    int num_elements = 5;

    printf("Displaying Scores:\n");

    /* SƏHV: i <= num_elements şərti yazılıb. 
       Massiv 0-dan 4-ə qədərdir, lakin döngü 5-ci indeksə (yaddaşın boş yerinə) 
       daxil olmağa çalışır. Bu, "Garbage value" çapına və ya crash-ə səbəb olur.
    */
    for (int i = 0; i <= num_elements; i++) {
        printf("Score %d: %d\n", i + 1, scores[i]);
        total_score += scores[i];
    }

    float average = (float)total_score / num_elements;
    printf("\nTotal: %d", total_score);
    printf("\nAverage Score: %.2f\n", average);

    return 0;
}
