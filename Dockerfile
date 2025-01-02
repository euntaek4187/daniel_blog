# Python 이미지 사용
FROM python:3.8-slim

# 작업 디렉토리 설정
WORKDIR /app

# 로컬의 코드 복사
COPY . .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn 실행 명령어
CMD ["gunicorn", "daniel_blog.wsgi:application", "--bind", "127.0.0.0:$8000"]
