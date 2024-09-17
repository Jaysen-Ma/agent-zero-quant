# Use the latest slim version of Debian
FROM debian:bookworm-slim

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    nodejs \
    npm \
    openssh-server \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Set up SSH
RUN mkdir /var/run/sshd && \
    echo 'root:toor' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create and activate Python virtual environment
# Set up a Python virtual environment
ENV VIRTUAL_ENV=/opt/venv
# Create a new virtual environment in the specified directory
RUN python3 -m venv $VIRTUAL_ENV
# Add the virtual environment's bin directory to the PATH
# This ensures that the virtual environment's Python is used
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy initial .bashrc with virtual environment activation to a temporary location
COPY .bashrc /etc/skel/.bashrc

# Copy the script to ensure .bashrc is in the root directory
COPY initialize.sh /usr/local/bin/initialize.sh
RUN chmod +x /usr/local/bin/initialize.sh

# Copy requirements file
COPY quant_requirements.txt .

# Install dependencies
# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install core data manipulation libraries
RUN pip install numpy==1.26.4 pandas==2.1.4 scipy==1.14.1 polars==1.6.0

# Install quant-specific libraries
RUN pip install vectorbt==0.26.2 yfinance==0.2.43 pandas_ta==0.3.14b0 backtrader==1.9.78.123 arcticdb==4.5.0 ccxt==4.4.3 python-binance==1.0.19 riskfolio-lib==4.4.2

# Install machine learning libraries
RUN pip install scikit-learn==1.3.2 xgboost==2.0.3 catboost==1.2.2 lightgbm==4.1.0 prophet==1.1.5

# Install deep learning libraries
RUN pip install tensorflow==2.15.0 torch==2.2.1 keras==2.15.0 gym==0.26.2

# Install optimization and statistical libraries
RUN pip install numba==0.58.1 optuna==3.4.0 scikit-optimize==0.9.0 statsmodels==0.14.1 dask==2024.9.0

# Install additional ML tools
RUN pip install joblib==1.4.2 hyperopt==0.2.7 deap==1.4

# Install visualization libraries
RUN pip install matplotlib==3.8.2 seaborn==0.13.0 plotly==5.19.0

# Install Utilities
RUN pip install pytz==2023.3.post1 requests==2.32.3 nbformat==5.10.4 pydantic==2.9.0

# Install Scraping libraries
RUN pip install beautifulsoup4==4.12.3 scrapy==2.11.2

# Install other NLP libraries
RUN pip install nltk==3.9.1 spacy==3.7.6 transformers==4.44.2

# Clean up
RUN pip cache purge && \
    rm quant_requirements.txt
    
# Expose SSH port
EXPOSE 22

# Init .bashrc
CMD ["/usr/local/bin/initialize.sh"]

