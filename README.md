# MFA(Montreal Forced Aligner) 사용법

텍스트(txt)과 음성(mp3)으로 자막(lrc)을 만드는 샘플입니다.

Docker를 이용하여 모든 OS에서 테스트 가능합니다.

<br>

## requirement

- [Docker](https://www.docker.com/)

<br>

## 실행 순서

한글 텍스트와 음성으로 자막을 만듭니다.


쉘명령 시작

> 이미 만든 container가 있는 경우
> ```sh
> docker container start mfa
> docker exec -it mfa bash
> ```

```sh
docker run -it --name mfa -v .:/data mmcauliffe/montreal-forced-aligner:latest
```

<br>

한글 모델 다운로드 (실행 후 조금 기다려야함)

```sh
mfa model download acoustic korean_mfa
mfa model download dictionary korean_mfa
```

> 다운로드 잘 되었는지 확인
> ```sh
> mfa model inspect acoustic korean_mfa
> mfa model inspect dictionary korean_mfa
> ```


> 일본어 & 영어
> ```sh
> mfa model download acoustic english_mfa
> mfa model download dictionary english_mfa
> mfa model download acoustic japanese_mfa
> mfa model download dictionary japanese_mfa
> ```

> 중국어 간체
> ```sh
> mfa model download acoustic mandarin_mfa
> mfa model download dictionary mandarin_china_mfa
> pip install spacy-pkuseg dragonmapper hanziconv
> ```
> 중국어에서 tokenizer 성능을 위해서 python library 설치 필요


<br>

align 시작

> --clean 으로 캐시삭제 후 재생성

```sh
mfa align /data/sample/ko korean_mfa korean_mfa /data/sample/ko/output --clean
```

> 영어 & 일본어
> ```sh
> mfa align /data/sample/en english_mfa english_mfa /data/sample/en/output --clean
> mfa align /data/sample/ja japanese_mfa japanese_mfa /data/sample/ja/output --clean
> ```

> 중국어 간체
> ```sh
> mfa align /data/sample/zh-cn/aegibong mandarin_china_mfa mandarin_mfa /data/sample/zh-cn/aegibong/output --clean
> ```

<br>

# textgrid to lrc

실행

```sh
pip install textgrid

python /data/textgrid_2_lrc.py --dir=/data/sample/ko/output
```

<br>

# 문장 단위로 쪼개기

docuparser에서 `extract_lrc.py`를 실행하여 lrc를 문장단위로 나눌 수 있다.

<br>

# 테스트

[온라인](https://seinopsys.dev/lrc) 에서 하고 있음. 2024-11-12 기준으로 조사해보니 우리가 업로드한 파일을 몰래 가져간다던지 하는 짓은 안함.

<br>

# license
MIT