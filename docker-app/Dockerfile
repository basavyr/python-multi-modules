FROM basavyr/pyenv-ubuntu

SHELL ["/bin/bash", "-c"]

ENV PYTHON_VERSION 3.8.6
ENV PATH=/root/.pyenv/plugins/pyenv-virtualenv/shims:/root/.pyenv/shims:/root/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PYTHONPATH "${PYTHONPATH}:/usr/local/bin"

WORKDIR /home/basayr

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

# CMD ["/bin/bash","./tests/test_app3.py"]
CMD ["/bin/bash","./tests.sh"]