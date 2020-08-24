FROM python:3.6-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY src/ /app
WORKDIR /app

CMD ["pytest", "-v", "-m", "--html=/Test_Report/test_services.html", "--self-contained-html", "/Test_Scripts/"]
