FROM python:3.11-alpine

RUN apk add --no-cache texlive

WORKDIR /app

COPY latex_gen_nikitakeba /app/latex_gen_nikitakeba
RUN pip install /app/latex_gen_nikitakeba

COPY task_2.py /app/
COPY artifacts/superman.png /app/artifacts/

RUN mkdir -p /app/artifacts

CMD ["python", "task_2.py"]
