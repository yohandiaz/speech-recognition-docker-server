FROM alpine:latest

# Install shell
RUN apk update && apk add --no-cache bash

# Set the default command to launch a shell
CMD ["bash"]