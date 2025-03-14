
# Python 3.11을 기반으로 하는 공식 이미지 사용
FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# 로컬 코드 및 종속성 파일 복사
COPY . /app

# 필요 패키지 설치
COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt

# FastAPI 및 필요 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt


# 애플리케이션 코드 복사
COPY saved_model.pkl .

# FastAPI 실행 (uvicorn 사용)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
