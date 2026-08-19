#베이스 이미지 지정
FROM python:3.11-slim

#컨테이너 안에서 작업할 디렉토리 지정
WORKDIR /app

#requirements.txt만 먼저 복사하고 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#나머지 프로젝트 파일 전체 복사
COPY . .

#컨테이너가 몇 번 포트를 쓰는지 명시
EXPOSE 8501

#컨테이너 시작할 때 실행할 명령어
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
