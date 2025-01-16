FROM alpine:3.20

# Create searxng user and group first
RUN addgroup -g 977 searxng && \
    adduser -u 977 -D -h /usr/local/searxng -s /bin/sh -G searxng searxng

# Create the /etc/searxng directory and assign ownership
RUN mkdir -p /etc/searxng && \
    chown -R searxng:searxng /etc/searxng

# Set entrypoint and expose port
ENTRYPOINT ["/sbin/tini","--","/usr/local/searxng/dockerfiles/docker-entrypoint.sh"]
EXPOSE 8080
VOLUME /etc/searxng

# Set environment variables for searxng configuration
ENV INSTANCE_NAME=searxng \
    AUTOCOMPLETE= \
    BASE_URL= \
    MORTY_KEY= \
    MORTY_URL= \
    SEARXNG_SETTINGS_PATH=/etc/searxng/settings.yml \
    UWSGI_SETTINGS_PATH=/etc/searxng/uwsgi.ini \
    UWSGI_WORKERS=%k \
    UWSGI_THREADS=4

# Set working directory
WORKDIR /usr/local/searxng

# Copy requirements.txt
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN apk add --no-cache -t build-dependencies \
    build-base \
    py3-setuptools \
    python3-dev \
    libffi-dev \
    libxslt-dev \
    libxml2-dev \
    openssl-dev \
    tar \
    git \
 && apk add --no-cache \
    ca-certificates \
    python3 \
    py3-pip \
    libxml2 \
    libxslt \
    openssl \
    tini \
    uwsgi \
    uwsgi-python3 \
    brotli \
 && pip3 install --break-system-packages --no-cache -r requirements.txt \
 && apk del build-dependencies \
 && rm -rf /root/.cache

# Copy the Docker files and source code
COPY --chown=searxng:searxng dockerfiles ./dockerfiles
COPY --chown=searxng:searxng searx ./searx

# Create /etc/searxng/ and copy necessary files
COPY --chown=searxng:searxng dockerfiles/uwsgi.ini /etc/searxng/uwsgi.ini
COPY --chown=searxng:searxng searx/settings.yml /etc/searxng/settings.yml

# Set timestamps for files to avoid rebuilds and prevent stale cache
ARG TIMESTAMP_SETTINGS=0
ARG TIMESTAMP_UWSGI=0
ARG VERSION_GITCOMMIT=unknown

RUN su searxng -c "/usr/bin/python3 -m compileall -q searx" \
 && touch -c --date=@${TIMESTAMP_SETTINGS} searx/settings.yml \
 && touch -c --date=@${TIMESTAMP_UWSGI} dockerfiles/uwsgi.ini \
 && find /usr/local/searxng/searx/static -a \( -name '*.html' -o -name '*.css' -o -name '*.js' \
    -o -name '*.svg' -o -name '*.ttf' -o -name '*.eot' \) \
    -type f -exec gzip -9 -k {} \+ -exec brotli --best {} \+

# Add metadata labels for the image
ARG LABEL_DATE=
ARG GIT_URL=unknown
ARG SEARXNG_GIT_VERSION=unknown
ARG SEARXNG_DOCKER_TAG=unknown
ARG LABEL_VCS_REF=
ARG LABEL_VCS_URL=
LABEL maintainer="Fondness https://github.com/BalaPriyan" \
      description="A privacy-respecting, hackable metasearch engine." \
      version="${SEARXNG_GIT_VERSION}" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.name="Fondness" \
      org.label-schema.version="${SEARXNG_GIT_VERSION}" \
      org.label-schema.url="${LABEL_VCS_URL}" \
      org.label-schema.vcs-ref=${LABEL_VCS_REF} \
      org.label-schema.vcs-url=${LABEL_VCS_URL} \
      org.label-schema.build-date="${LABEL_DATE}" \
      org.label-schema.usage="https://github.com/searxng/searxng-docker" \
      org.opencontainers.image.title="searxng" \
      org.opencontainers.image.version="${SEARXNG_DOCKER_TAG}" \
      org.opencontainers.image.url="${LABEL_VCS_URL}" \
      org.opencontainers.image.revision=${LABEL_VCS_REF} \
      org.opencontainers.image.source=${LABEL_VCS_URL} \
      org.opencontainers.image.created="${LABEL_DATE}" \
      org.opencontainers.image.documentation="https://github.com/searxng/searxng-docker"

