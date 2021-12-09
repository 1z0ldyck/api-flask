FROM alpine:3.14

RUN mkdir /home/app

COPY /app /home/app

WORKDIR /home/app

RUN apk add --update --no-cache python3 py3-pip && pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]