FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app_utils.py /app/app_utils.py
COPY crud.py /app/crud.py
COPY database.py /app/database.py
COPY main.py /app/main.py
COPY models.py /app/models.py
COPY schemas.py /app/schemas.py
COPY test_unit.py /app/test_unit.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8084"]
#CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
