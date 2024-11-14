from textgrid import TextGrid
import datetime
from pathlib import Path

import click

@click.command()
@click.option('--dir', help='The folder contains TextGrid files')
def commandline(dir):
    cnt = 0
    for type in [r'*.TextGrid']:
        for f in Path(dir).rglob(type):
            convert((str(f)))
            cnt += 1
    
    if cnt == 0:
        print('No file to convert. please check the file exists.')
    else:
        print(f'converted {cnt} file(s)')


def convert(arg):
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
    commandline()
