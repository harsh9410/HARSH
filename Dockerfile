FROM redhat/ubi8

RUN yum install python3 -y &&  pip install flask

COPY first.py /app.py

CMD ["python3","app.py"]
