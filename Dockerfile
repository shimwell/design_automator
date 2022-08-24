# build with
# docker build -t shimwell/design_automator .

FROM continuumio/miniconda3:4.12.0
# FROM condaforge/mambaforge-pypy3:4.9.2-7

RUN apt-get --allow-releaseinfo-change update
RUN apt-get --yes update && apt-get --yes upgrade

RUN apt-get --yes install libeigen3-dev \
                        #   sudo  \
                          # sudo is needed during the NJOY install
                          git \
                          wget \
                          gfortran \
                          g++ \
                          mpich \
                          libmpich-dev \
                          libhdf5-serial-dev \
                          libhdf5-mpich-dev \
                          hdf5-tools \
                          imagemagick \
                          cmake \
                          # libnetcdf-dev is needed to allow NETCDF on MOAB which helps with tet meshes in OpenMC
                          libnetcdf-dev \
                          # libtbb-dev required for DAGMC
                          libtbb-dev \
                          # libglfw3-dev required for DAGMC
                          libglfw3-dev \
                          # needed for CadQuery functionality
                          libgl1-mesa-glx \
                          # needed for CadQuery functionality
                          libgl1-mesa-dev \
                          # needed for CadQuery functionality
                          libglu1-mesa-dev \
                          # needed for CadQuery functionality
                          freeglut3-dev \
                          # needed for CadQuery functionality
                          libosmesa6 \
                          # needed for CadQuery functionality
                          libosmesa6-dev \
                          # needed for CadQuery functionality
                          libgles2-mesa-dev \
                          # needed for Gmsh functionality
                          libxft2

# installing cadquery and jupyter
RUN conda install -c conda-forge -c python python=3.8

RUN conda install -c fusion-energy -c cadquery -c conda-forge paramak==0.8.2

# python packages from the neutronics workflow
RUN pip install neutronics_material_maker[density] \
                remove_dagmc_tags \
                openmc-plasma-source \
                openmc-dagmc-wrapper \
                openmc-tally-unit-converter \
                regular_mesh_plotter \
                spectrum_plotter \
                openmc_source_plotter

# Python libraries used in the workshop
RUN pip install cmake\
# new version of cmake needed for openmc compile
                plotly \
                tqdm \
                scikit-optimize \
                scikit-opt \
                adaptive \
                vtk \
                itkwidgets \
                pytest \
                holoviews \
                ipywidgets \
# cython is needed for moab
                cython \
                nest_asyncio \
                jupyterlab \
                jupyter-cadquery

# needed for openmc
RUN pip install --upgrade numpy


# Clone and install MOAB
RUN mkdir MOAB && \
    cd MOAB && \
    git clone  --single-branch --branch 5.3.1 --depth 1 https://bitbucket.org/fathomteam/moab.git && \
    mkdir build && \
    cd build && \
    cmake ../moab -DENABLE_HDF5=ON \
                  -DENABLE_NETCDF=ON \
                  -DENABLE_FORTRAN=OFF \
                  -DENABLE_BLASLAPACK=OFF \
                  -DBUILD_SHARED_LIBS=OFF \
                  -DCMAKE_INSTALL_PREFIX=/MOAB && \
    make -j &&  \
    make -j install && \
    cmake ../moab -DENABLE_HDF5=ON \
                  -DENABLE_PYMOAB=ON \
                  -DENABLE_FORTRAN=OFF \
                  -DBUILD_SHARED_LIBS=ON \
                  -DENABLE_BLASLAPACK=OFF \
                  -DCMAKE_INSTALL_PREFIX=/MOAB && \
    make -j install && \
    cd pymoab && \
    bash install.sh && \
    python setup.py install
    # the following rm command appears to remove libraries that are need to use
    # pymoab so this has been commented out for now
    # rm -rf /MOAB/moab /MOAB/build


ENV PATH=$PATH:/MOAB/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/MOAB/lib


# DAGMC version develop install from source
RUN mkdir DAGMC && \
    cd DAGMC && \
    git clone --single-branch --branch v3.2.1 --depth 1 https://github.com/svalinn/DAGMC.git && \
    mkdir build && \
    cd build && \
    cmake ../DAGMC -DBUILD_TALLY=ON \
                   -DMOAB_DIR=/MOAB \
                   -DBUILD_STATIC_EXE=OFF \
                   -DBUILD_STATIC_LIBS=OFF \
                   -DCMAKE_INSTALL_PREFIX=/DAGMC/ && \
    make -j install && \
    rm -rf /DAGMC/DAGMC /DAGMC/build

ENV PATH=$PATH:/DAGMC/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/DAGMC/lib



# installs OpenMc from source
RUN cd /opt && \
    # switch back to tagged version when 0.13.1 is released as develop depletion is used
    # git clone --single-branch --branch v0.13.0 --depth 1 https://github.com/openmc-dev/openmc.git && \
    git clone --single-branch --branch develop --depth 1 https://github.com/openmc-dev/openmc.git && \
    cd openmc && \
    mkdir build && \
    cd build && \
    cmake -DOPENMC_USE_DAGMC=ON \
          -DDAGMC_ROOT=/DAGMC \
          -DHDF5_PREFER_PARALLEL=OFF .. && \
    make -j && \
    make -j install && \
    cd /opt/openmc/ && \
    pip install .

# installs TENDL and ENDF nuclear data. Performed after openmc install as
# openmc is needed to write the cross_Sections.xml file
RUN pip install openmc_data_downloader && \
    openmc_data_downloader -d nuclear_data -l ENDFB-7.1-NNDC TENDL-2019 -p neutron photon -e all -i H3 --no-overwrite

