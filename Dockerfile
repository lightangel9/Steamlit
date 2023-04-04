# ใช้ image ของ python 3.9 กับ Ubuntu 20.04
FROM python:3.9-buster


# ติดตั้ง OpenCV dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libgtk-3-dev \
    libpng-dev \
    libjpeg-dev \
    libwebp-dev \
    libopenexr-dev \
    libtiff-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libatlas-base-dev \
    gfortran \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*
    
    # ติดตั้ง OpenCV และ dependencies อื่นๆ ด้วย pip
RUN pip install --upgrade pip && \
    pip install opencv-python-headless streamlit

# ประกาศพอร์ตที่ Streamlit จะใช้งาน
EXPOSE 8501

#Running the streamlit app
ENTRYPOINT ["streamlit", "run", "--server.maxUploadSize=5"]
CMD ["main/streamlit_app.py"]
