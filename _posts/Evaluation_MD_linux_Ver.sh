#!/bin/bash

# 현재 디렉터리의 모든 하위 폴더를 검사
for dir in */; do
    # 파일 개수를 세기
    file_count=$(find "$dir" -type f | wc -l)

    # 결과 출력
    if [ "$file_count" -ge 10 ]; then
        echo "${dir%/}: OK (${file_count} files)"
    else
        echo "${dir%/}: 문제 있음 (${file_count} files)"
    fi

done