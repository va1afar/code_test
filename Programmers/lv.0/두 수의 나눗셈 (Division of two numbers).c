// link :: https://school.programmers.co.kr/learn/courses/30/lessons/120806

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2) {
    int answer = 0;

    answer = ((double)num1 / num2) * 1000;
    
    return answer;
}
