FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["takeQuiz.py"]
ENTRYPOINT ["python3"]
