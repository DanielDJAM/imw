from fabric.api import env, cd, local, run

# nombre de la máquina de producción
env.hosts = ['vmweb.alu5894.es']


def deploy():
    local('git push')
    with cd('~/webapps/myweb'):
      run('git pull')
    run('supervisorctl restart myweb')
