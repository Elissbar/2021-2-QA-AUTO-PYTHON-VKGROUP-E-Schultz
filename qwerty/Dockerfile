FROM python:3.8

ADD req.txt /req.txt

RUN pip3 install -r /req.txt && rm -f /req.txt

ADD tests /tests
WORKDIR /tests

RUN pytest -s -l -v code/test_first.py
