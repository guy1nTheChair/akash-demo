FROM python:3.8-alpine

COPY . .

RUN pip3 install -q requirements.txt

RUN chmod +x startup.sh

EXPOSE 5000

ENTRYPOINT [ "sh", "startup.sh" ]