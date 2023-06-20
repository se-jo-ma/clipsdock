FROM alpine:latest


RUN mkdir /orq \
&& apk --update add --no-cache \
    build-base \
    gcc \
    git \
    make \
    nano \
    python3 \
    py3-cffi \
    python3-dev \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    unzip \
    wget \
    zip \
&& pip3 install --upgrade pip \
&& git clone https://github.com/noxdafox/clipspy.git

COPY ./orq/ /orq/

# Build and install CLIPS and CLIPSPy
WORKDIR /clipspy
RUN make \
    && make install

# Lazy workaround to add clips to PATH variable
ENV PATH="${PATH}:/clipspy/clips_source"

WORKDIR /orq

# Used to keep the container running
CMD [ "/bin/sh" ]
