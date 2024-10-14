FROM python:3.9-slim as builder

RUN apt-get update && apt-get install -y \
    build-essential cmake git pkg-config \
    libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev libjpeg-dev libpng-dev

WORKDIR /opencv_build
RUN git clone https://github.com/opencv/opencv.git
RUN git clone https://github.com/opencv/opencv_contrib.git

WORKDIR /opencv_build/opencv/build
RUN cmake -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=/opencv_build/opencv_contrib/modules \
    -D BUILD_EXAMPLES=OFF ..
RUN make -j$(nproc)
RUN make install

FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libgtk2.0-dev \
    libjpeg-dev libpng-dev

COPY --from=builder /usr/local/ /usr/local/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app

CMD ["python", "main.py"]
