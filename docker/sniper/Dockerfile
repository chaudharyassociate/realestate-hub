# Sniper - Automated Pentesting Framework
FROM kalilinux/kali-rolling:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nmap \
    masscan \
    gobuster \
    nikto \
    sqlmap \
    wget \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /opt/sniper

# Copy sniper configuration
COPY sniper-config.py /opt/sniper/
COPY entrypoint.sh /opt/sniper/

# Make entrypoint executable
RUN chmod +x /opt/sniper/entrypoint.sh

# Install Python dependencies
RUN pip3 install requests beautifulsoup4 python-nmap

# Expose API port
EXPOSE 8080

# Set entrypoint
ENTRYPOINT ["/opt/sniper/entrypoint.sh"]