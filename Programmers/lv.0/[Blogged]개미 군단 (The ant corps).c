// link :: https://school.programmers.co.kr/learn/courses/30/lessons/120837

// Blogged post link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-0-the-ant-corps-94c1b6c1aee

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int hp) {
    int answer = 0;

    answer += (hp/5);
    hp %= 5;
        
    answer += (hp/3);
    hp %= 3;
    
    answer += (hp/1);
    hp %= 1;
        
    return answer;
}
