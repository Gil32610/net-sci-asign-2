FROM python:3.11-bookworm

# Install standard APT packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential \
    texlive-xetex \
    texlive-latex-extra \
    texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /workspace

# Copy requirements directly into /workspace and install them
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt