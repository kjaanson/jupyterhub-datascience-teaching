import os
from jupyter_client.localinterfaces import public_ips

ip = public_ips()[0]

c.Application.log_level = 'DEBUG'

c.JupyterHub.hub_ip = ip
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 443

c.JupyterHub.cookie_secret_file = '/opt/jupyterhub/jupyterhub_cookie_secret'
c.JupyterHub.db_url = 'sqlite:////opt/jupyterhub/jupyterhub.sqlite'
c.JupyterHub.hub_port = 8181

c.JupyterHub.ssl_key = '/opt/jupyterhub/ssl/key.pem'
c.JupyterHub.ssl_cert = '/opt/jupyterhub/ssl/cert.pem'


c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

c.DockerSpawner.image = 'jupyter/datascience-notebook:4cdbc9cdb7d1'

# This should limit the env variables from jupyterhub to jupter notebook. 
# Not sure if it works when notebook is started by sudospawner.
c.Spawner.env_keep = ['PATH',
                      'PYTHONPATH',
                      'CONDA_ROOT',
                      'CONDA_DEFAULT_ENV',
                      'VIRTUAL_ENV',
                      'LANG',
                      'LC_ALL',
                      'SPARK_HOME',
                      'SPARK_LOG_DIR',
                      'SPARK_CONF_DIR',
                      'SPARK_WORKER_DIR',
                      'SPARK_EXECUTOR_CORES',
                      'SPARK_EXECUTOR_MEMORY',
                      'SPARK_DRIVER_MEMORY',
                      'PYSPARK_PYTHON',
                      'PYSPARK_DRIVER_PYTHON'
                      ]

c.Authenticator.admin_users = {'kajaan','juliiv'}
