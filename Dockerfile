FROM python:3.11.2

WORKDIR /code

EXPOSE 5050

COPY ./requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ENTRYPOINT ["./entrypoint_backend.sh"]

COPY . .

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]