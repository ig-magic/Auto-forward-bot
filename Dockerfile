# ✅ Use supported Debian base (FIXES your error)
FROM python:3.10-slim-bullseye

# ✅ Environment safety
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# ✅ Install system dependencies
RUN apt-get update \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

# ✅ Set working directory (replaces mkdir + cd)
WORKDIR /VJ-Forward-Bot

# ✅ Copy requirements first (better caching)
COPY requirements.txt .

# ✅ Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# ✅ Copy full project
COPY . .

# ✅ Start gunicorn + bot (same behavior as your old CMD, but safer)
CMD ["bash", "-c", "gunicorn app:app --bind 0.0.0.0:8000 & python3 main.py"]
