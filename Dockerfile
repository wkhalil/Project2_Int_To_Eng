FROM python:3.6-slim
MAINTAINER yuweiz<yz667@duke.edu>

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY IntToString.py IntToString.py
COPY main.py main.py

CMD ["python3", "main.py"]