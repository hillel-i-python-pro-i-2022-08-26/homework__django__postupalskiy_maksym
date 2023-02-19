FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt


COPY --chown=${USER} --chmod=755 ./docker/app/start.sh /start.sh
COPY --chown=${USER} --chmod=755 ./docker/app/entrypoint.sh /entrypoint.sh

COPY --chown=${USER} ./manage.py manage.py
COPY --chown=${USER} ./Makefile Makefile

# Core Apps [START]
COPY --chown=${USER} ./apps apps
COPY --chown=${USER} ./contacts contacts
COPY --chown=${USER} ./core core
COPY --chown=${USER} ./greetings greetings
COPY --chown=${USER} ./session session
COPY --chown=${USER} ./users_admin users_admin
COPY --chown=${USER} ./users_generator users_generator
COPY --chown=${USER} ./users users
COPY --chown=${USER} ./middlewares middlewares
COPY --chown=${USER} ./crud_rest_framework crud_rest_framework
# Core Apps [END]

# HTML/CSS [START]
COPY --chown=${USER} ./templates templates
COPY --chown=${USER} ./static static
# HTML/CSS [END]

USER ${USER}

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]