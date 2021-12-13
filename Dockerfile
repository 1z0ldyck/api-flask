FROM python

RUN mkdir /home/app

COPY /app /home/app

WORKDIR /home/app

RUN pip3 install -r requirements.txt
RUN export FLASK_APP="app.app"

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]