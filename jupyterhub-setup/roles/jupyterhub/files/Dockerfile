FROM jupyter/datascience-notebook:4cdbc9cdb7d1

USER $NB_UID

RUN conda install --quiet --yes -c bioconda snakemake fastqc trimmomatic salmon star multiqc blast bioconductor-deseq2 && \
    conda install -c bioconda ucsc-bigwigtowig && \
    conda install -yq -c conda-forge nbrsessionproxy && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# install rstudio-server
USER root
RUN apt-get update && \
    curl --silent -L --fail https://download2.rstudio.org/rstudio-server-1.1.419-amd64.deb > /tmp/rstudio.deb && \
    echo '24cd11f0405d8372b4168fc9956e0386 /tmp/rstudio.deb' | md5sum -c - && \
    apt-get install -y /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean

ENV PATH=$PATH:/usr/lib/rstudio-server/bin
USER $NB_USER

