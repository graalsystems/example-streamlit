# Streamlit example

This repo contains the code for a simple Streamlit application. The application contains simple Streamlit components such as a `text_input` and a `slider`. The application also contains a `checkbox` example, a `button` and a `selectbox`.

The application can be deployed in a Docker container. The Dockerfile is included in the repo. The application can be run locally using the following command:

```bash
streamlit run app.py --host 0.0.0.0 --port 8501
```

You can also run the application in a Docker container using the following command:

```bash
docker build -t streamlit-example .
docker run -p 8501:8501 streamlit-example
```

Finally, the application can be deployed on a Kubernetes cluster using the following command:

```bash
kubectl apply -k
```