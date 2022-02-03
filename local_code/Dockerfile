FROM python:3.8

ADD ../venv/req.txt /req.txt

RUN pip3 install -r /requerements.txt && rm -f /requerements.txt

ADD ../tests /tests
WORKDIR /tests

RUN pytest -s -l -v tests/test_first.py
