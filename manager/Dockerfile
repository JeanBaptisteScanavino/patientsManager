FROM python:3.10.6-slim


ENV PYTHONUNBUFFERED 1
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY ./requirements.txt /etc/requirements/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install -r /etc/requirements/requirements.txt

COPY ./start.sh ./
RUN chmod +x /start.sh

ENV PATH="/home/app_user/.local/bin:${PATH}"

CMD ["./start.sh"]