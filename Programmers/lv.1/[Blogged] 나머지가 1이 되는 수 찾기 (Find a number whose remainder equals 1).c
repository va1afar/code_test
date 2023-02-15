// link :: https://school.programmers.co.kr/learn/courses/30/lessons/87389

// blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-find-a-number-whose-remainder-equals-1-5acd1b7ae6f6

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int x = 2;
    
    while((n%x)!=1){
        x++;
    }
    
    answer = x ;
    
    return answer;
}
