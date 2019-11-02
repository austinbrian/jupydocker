FROM python:3.6-slim
RUN pip install jupyter numpy matplotlib rise
RUN mkdir notebooks
WORKDIR notebooks/
COPY . .

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "/notebooks/JupyDockerSlides.ipynb","--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root","--NotebookApp.token='pydata'"]



