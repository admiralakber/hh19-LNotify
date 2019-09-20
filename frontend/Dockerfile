FROM node:10-alpine

# Create and define the node_modules's cache directory.
RUN mkdir -p /usr/src/cache
WORKDIR /usr/src/cache

# Install the application's dependencies into the node_modules's cache directory.
RUN npm install -g gatsby-cli 
COPY app/package.json ./
COPY app/package-lock.json ./
RUN npm install

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY app /usr/src/app

EXPOSE 8000

CMD ["sh", "/usr/src/app/entrypoint.sh"]