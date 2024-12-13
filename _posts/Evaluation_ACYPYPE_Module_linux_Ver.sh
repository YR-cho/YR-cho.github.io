#!/bin/bash

# 현재 디렉터리의 모든 하위 폴더를 검사
for dir in */; do
    # POC.acpype 폴더 경로 설정
    target_folder="${dir}POC.acpype"
    
    # POC.acpype 폴더가 존재하는지 확인
    if [ -d "$target_folder" ]; then
        # 파일 개수를 세기
        file_count=$(find "$target_folder" -type f | wc -l)
        
        # 결과 출력
        if [ "$file_count" -ge 10 ]; then
            echo "${dir%/}: OK (${file_count} files)"
        else
            echo "${dir%/}: 문제 있음 (${file_count} files)"
        fi
    else
        echo "${dir%/}: POC.acpype 폴더가 존재하지 않습니다."
    fi
done
