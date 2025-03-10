#! /bin/bash

# if not yet, please build image:
# singularity build brics_jupyterhub_rocky.sif container/brics_jupyterhub_rocky.def

singularity exec \
  --bind config:/srv/jupyterhub:rw \
  --bind notebooks:/tmp/admin/notebooks:rw \
  brics_jupyterhub_rocky.sif \
  jupyterhub -f /srv/jupyterhub/jupyterhub_config.py > jupyterhub.log 2>&1
