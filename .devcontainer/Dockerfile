# build with
# docker build -t design_automator .

FROM continuumio/miniconda3:4.12.0
# FROM condaforge/mambaforge-pypy3:4.9.2-7

RUN apt-get --allow-releaseinfo-change update
RUN apt-get --yes update && apt-get --yes upgrade
RUN apt-get install -y libgl1-mesa-glx libgl1-mesa-dev libglu1-mesa-dev  freeglut3-dev libosmesa6 libosmesa6-dev libgles2-mesa-dev imagemagick

RUN conda config --add channels conda-forge
RUN conda config --set channel_priority strict

# using mamba to avoid tempest error in conda install dagmc
RUN conda install mamba -y
RUN mamba install gxx -y
RUN mamba install cmake -y
RUN mamba install make -y
RUN mamba install binutils -y
RUN mamba install -c conda-forge dagmc=3.2.2 -y

RUN git clone --single-branch --branch develop --depth 1 https://github.com/openmc-dev/openmc.git
RUN cd openmc && \
    mkdir build && \
    cd build && \
    cmake -DOPENMC_USE_DAGMC=ON ..  && \
    make -j && \
    make -j install && \
    cd /openmc/ && \
    pip install .
RUN mamba install -c fusion-energy -c cadquery -c conda-forge paramak=0.8.3 -y