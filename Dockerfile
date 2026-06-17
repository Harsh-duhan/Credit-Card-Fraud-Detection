FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    MPLBACKEND=Agg

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY Credit_card_fraud_detection.py .
COPY credit_card_fraud_model.pkl .

RUN useradd --create-home appuser
USER appuser

CMD ["python", "Credit_card_fraud_detection.py"]
