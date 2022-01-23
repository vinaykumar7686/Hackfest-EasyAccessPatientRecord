FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY /requirements.txt /django/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /django/
EXPOSE 8000
RUN chmod +x /django/start.sh
CMD /django/start.sh
