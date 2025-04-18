FROM pytorch/pytorch:2.2.1-cuda11.8-cudnn8-runtime

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "run.sh"]