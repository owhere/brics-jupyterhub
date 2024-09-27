import os
import logging
import sys

from dummyauthenticator import DummyAuthenticator

# Set the authenticator class to DummyAuthenticator for testing
c.JupyterHub.authenticator_class = DummyAuthenticator
c.Authenticator.admin_users = {'admin'}
c.Authenticator.allowed_users = {'admin'}

c = get_config()

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Log the final authenticator setup
logger.info("Using NoPasswordPAMAuthenticator for passwordless access")


# Log the final authenticator setup
logger.info("Assigned NoPasswordPAMAuthenticator")

# URL config
c.ConfigurableHTTPProxy.api_url = 'http://127.0.0.1:8018'
c.JupyterHub.bind_url = 'http://127.0.0.1:38024'

# Spawner settings
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'
c.Spawner.default_url = '/lab'
c.Spawner.notebook_dir = '~/notebooks'

c.JupyterHub.log_level = 'DEBUG'
