FROM continuumio/miniconda3

# Setting up working directory 
RUN mkdir /src
WORKDIR /src

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Create the VNC connection
ENV QT_QPA_PLATFORM=vnc
ENV XDG_RUNTIME_DIR=/tmp

# Activate the environment
SHELL ["conda", "run", "-n", "Epic_iO", "/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 libxcb-xinerama0 -y

ARG JSONFILE
ARG VIDEOFILE
ARG TRACK

CMD [ "conda", "run", "--no-capture-output", "-n", "Epic_iO", "python3", "main.py", "-j", "${JSONFILE}", "-v", "${VIDEOFILE}", "-t", "${TRACK}"]