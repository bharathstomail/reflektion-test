FROM python:3.6-alpine

USER root

COPY requirement.txt /
RUN mkdir -p /opt/Project_API
RUN chown root /opt/Project_API

#COPY src/ /app
COPY ./var/jenkins_home/workspace/Dockerizing_pipeline/Dockerfile/src/ /opt/Project_API/src
WORKDIR /opt/Project_API/src/
RUN pip install -r /requirement.txt
CMD ["pytest", "-v", "-m", "--html=/Test_Report/test_services.html", "--self-contained-html", "/Test_Scripts/"]
