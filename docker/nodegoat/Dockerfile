# OWASP NodeGoat - Vulnerable Node.js Application
FROM node:18-alpine

# Set working directory
WORKDIR /opt/nodegoat

# Clone NodeGoat repository
RUN apk add --no-cache git && \
    git clone https://github.com/OWASP/NodeGoat.git . && \
    npm install

# Expose application port
EXPOSE 4000

# Copy custom entrypoint
COPY entrypoint.sh /opt/nodegoat/
RUN chmod +x /opt/nodegoat/entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/opt/nodegoat/entrypoint.sh"]