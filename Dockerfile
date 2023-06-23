FROM python:3.9

ARG project_dir=/app/

COPY . $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
