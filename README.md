
# JupyterHub Singularity Container

This repository contains a Singularity definition file for building a JupyterHub container. The container is designed to run JupyterHub in a scalable and portable manner, allowing users to access Jupyter notebooks through a web interface.

## Prerequisites

- **Singularity**: Ensure you have Singularity installed on your system. You can find installation instructions [here](https://sylabs.io/guides/latest/user-guide/installation.html).


## Building the Container

To build the JupyterHub container, follow these steps:

1. **Clone the Repository:**
   Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Build the Container:**
 
```
singularity build brics_jupyterhub_rocky.sif container/brics_jupyterhub_rocky.def
```

## Configure JupyterHub

An example of config file is config/jupyterhub_config, which uses

1. DummyAuthenticator (no password)
2. SimpleLocalProcessSpawner (localhost spawner)

## Running JupyterHub

To run JupyterHub using the Singularity container, use the following command on ubuntu or rocky:

```bash
bash run_rocky.sh
```
or 
```bash
bash run_ubuntu.sh
```

This command will start JupyterHub and bind the configuration file located at `/srv/jupyterhub/jupyterhub_config.py`.

### Port Forwarding

To access JupyterHub from your local machine, you may need to forward the port:

1. **Using VSCode:**
   - Open the Command Palette (Ctrl + Shift + P).
   - Type `Remote-SSH: Forward a Port`.
   - Enter `8000` for the local port and the remote port that JupyterHub is running on (also typically `8000`).

2. **Manual SSH Port Forwarding:**
   You can also set up an SSH tunnel using the following command:
   ```bash
   ssh -L 8000:localhost:8000 your_username@remote_host
   ```
   Replace `your_username` and `remote_host` with your actual username and remote server address.

### Accessing JupyterHub

After starting JupyterHub and setting up port forwarding, open your web browser and navigate to:
```
http://localhost:38024
```

## Configuration

The JupyterHub configuration can be modified in the `jupyterhub_config.py` file located in the `/srv/jupyterhub/` directory. You can change various settings, including:

- Authentication methods
- User management
- Resource allocation
