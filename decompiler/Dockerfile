FROM ubuntu:latest

ARG FILES

# Set the working directory
WORKDIR /app
# and copy all relevant files
COPY ./xdr-decompiler /usr/bin/xdr
COPY ${FILES} /app

# Setup the
RUN chmod +x /usr/bin/xdr

# Set the entrypoint to the command line
ENTRYPOINT ["/bin/bash"]
