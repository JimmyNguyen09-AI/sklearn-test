FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
COPY hello.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY train.py .
CMD ["python", "train.py"]

# ENV 
# WORKDIR   ->THU MUC LAM VIEC
# RUN   ->CAI DAT
# CMD
# COPY  -> COPY FILE
# FROM  -> CHON IMAGE/ ENVIROMENT