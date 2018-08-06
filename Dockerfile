ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV WORKON_HOME=/tmp/venv
WORKDIR /app

COPY . .

RUN pip install -U pip wheel cython && \
    pip install pipenv && \
    pipenv --python /usr/bin/python3 && \
    pipenv install

CMD ['/bin/bash']
