FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "fastapiapp", "/bin/bash", "-c"]

COPY app.py .
COPY ./src ./src

EXPOSE 8000
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "fastapiapp", "python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]