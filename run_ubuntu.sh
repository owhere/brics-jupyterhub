# if not yet, please build image:
# singularity build --fakeroot brics_jupyterhub_ubuntu.sif container/brics_jupyterhub_ubuntu.def

singularity exec --env PYTHONNOUSERSITE=1 \
  --bind config:/srv/jupyterhub:rw \
  --bind notebooks:/tmp/admin/notebooks:rw \
  brics_jupyterhub_ubuntu.sif \
  jupyterhub -f /srv/jupyterhub/jupyterhub_config.py --debug > jupyterhub.log 2>&1