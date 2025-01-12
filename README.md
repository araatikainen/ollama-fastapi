# ollama-fastapi

Simple Chatbot using Ollama models, langchain ollama library, streamlit frontend and fastapi. Two models are run in containers (text and vision). Models can be set in .env file.

## Usage

### Install NVIDIA Container toolkit for gpu support

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

**Clonse the Repository**

```
git clone git@github.com:araatikainen/ollama-fastapi.git
cd ollama-fastapi

docker-compose build
docker-compose up
```

Pulling ollama models take few minutes first run, make sure you wait before generating.

