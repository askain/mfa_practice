from textgrid import TextGrid
import datetime
from pathlib import Path

# TextGrid 파일 경로와 LRC 파일 경로 지정
textgrid_dir = r"/data/sample/en/output"


def execute(arg):
    textgrid_path = arg
    lrc_path = textgrid_path.replace('.TextGrid', '.lrc', 1)
    # TextGrid 파일 읽기
    tg = TextGrid.fromFile(textgrid_path)

    # LRC 파일로 변환
    with open(lrc_path, "w", encoding="utf-8") as lrc_file:
        for interval in tg[0]:  # 첫 번째 tier 사용
            start_time = interval.minTime
            text = interval.mark.strip()
            
            if text:
                # 타임스탬프 포맷 [MM:SS.xx]
                minutes = int(start_time // 60)
                seconds = int(start_time % 60)
                milliseconds = int((start_time * 100) % 100)
                timestamp = f"[{minutes:02}:{seconds:02}.{milliseconds:02}]"
                
                # LRC 포맷에 맞게 작성
                lrc_file.write(f"{timestamp}{text}\n")

    print(f"{textgrid_path} -> {lrc_path}에 저장되었습니다.")

if __name__ == '__main__':
    for type in [r'*.TextGrid']:
        for f in Path(textgrid_dir).rglob(type):
            execute((str(f)))
