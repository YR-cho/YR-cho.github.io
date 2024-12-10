import os

def display_tree_with_file_count(base_path, indent=""):
    # 현재 디렉토리의 내용을 가져옴
    entries = os.listdir(base_path)
    file_count = len([entry for entry in entries if os.path.isfile(os.path.join(base_path, entry))])

    # 폴더 경로 출력 및 파일 개수 출력
    print(f"{indent}{os.path.basename(base_path)}/ ({file_count} files)")

    # 각 항목에 대해 재귀적으로 처리
    for entry in entries:
        entry_path = os.path.join(base_path, entry)
        if os.path.isdir(entry_path):
            display_tree_with_file_count(entry_path, indent + "│   ")

        elif os.path.isfile(entry_path):
            print(f"{indent}│   ├── {entry}")

# 기준 경로 설정 (현재 디렉토리 기준으로 설정)
base_path = "./"  # 원하는 경로로 변경하세요

# 트리 출력 실행
display_tree_with_file_count(base_path)
