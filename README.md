# Streamlit example (deprecated)

> **This repository is no longer maintained and is kept for reference only.** It is a generic
> Streamlit application deployed with plain Kubernetes manifests and does not use the graal
> Data Platform. For examples of graal jobs, see
> [graalsystems/examples](https://github.com/graalsystems/examples).

A small [Streamlit](https://streamlit.io) application showing a text input, a slider, a
checkbox, a button and a select box.

```bash
pip install -r requirements.txt
streamlit run main.py --server.address 0.0.0.0 --server.port 8501

docker build -t streamlit-example .
docker run -p 8501:8501 streamlit-example

kubectl apply -k kubernetes/
```
