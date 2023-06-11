FROM python:3.10

RUN mkdir /code

COPY .requirements.txt /code

RUN pip install -r requirements.txt

COPY /jewellery_shop /code

CMD [ "python3", "manage.py", "runserver" ]