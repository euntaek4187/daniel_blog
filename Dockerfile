# 베이스 이미지 선택
FROM python:3.10-slim

# 작업 디렉토리 생성
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . /app/

# 포트 노출
EXPOSE 8000

# 명령어 실행
CMD ["gunicorn", "daniel_blog.wsgi:application", "--bind", "0.0.0.0:8000"]
