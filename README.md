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

```sh
docker run -it -v .:/data mmcauliffe/montreal-forced-aligner:latest
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


일본어 & 영어

```sh
> mfa model download acoustic english_mfa
> mfa model download dictionary english_mfa
> mfa model download acoustic japanese_mfa
> mfa model download dictionary japanese_mfa
```

<br>

align 시작

```sh
mfa align /data/sample/ko korean_mfa korean_mfa /data/sample/ko/output
```

<br>

# textgrid to lrc

`textgrid_2_lrc.py`에서 경로 수정 필요

```python
textgrid_dir = r"/data/sample/ko/output"
```

실행

```sh
pip install textgrid

python textgrid_2_lrc.py
```

<br>

# 테스트

[온라인](https://seinopsys.dev/lrc) 에서 하고 있음. 2024-11-12 기준으로 서버에 파일을 업로드한다던지 하는 짓은 안함.

<br>

# license
MIT