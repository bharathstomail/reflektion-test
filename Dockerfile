FROM python:3.6-alpine

COPY requirement.txt /
RUN pip install -r /requirement.txt

COPY src/ /app
WORKDIR /app

CMD ["pytest", "-v", "-m", "--html=/Test_Report/test_services.html", "--self-contained-html", "/Test_Scripts/"]
