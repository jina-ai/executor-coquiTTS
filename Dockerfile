FROM jinaai/jina:latest

# install requirements before copying the workspace
COPY requirements.txt /requirements.txt
RUN apt-get update && apt-get install --no-install-recommends -y build-essential libsndfile1 && pip install --default-timeout=1000 --compile -r requirements.txt


# setup the workspace
COPY . /workspace
WORKDIR /workspace
RUN tts --text "Text for TTS"  # warmup

ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]
