FROM python:3.8

ADD requerements.txt /requerements.txt
ADD /api_client /code/api_client
ADD /orm /code/orm
ADD /tests /code/tests
ADD /ui /code/ui
ADD conftest.py /code

RUN pip3 install -r /requerements.txt && rm -f /requerements.txt
RUN ls -la /code
#RUN pytest -s -l -v /code/tests/tests.py


