FROM python:3.8

ADD requerements.txt /requerements.txt

ADD mock_vk_id.py /code/mock_vk_id.py

RUN pip3 install -r /req.txt && rm -f /req.txt

EXPOSE 5000

WORKDIR /code

CMD ["python3", "mock_vk_id.py"]
