FROM python:3.13.9-slim
COPY . /
RUN pip3 install flask
CMD ["python","Sequence.py"]
