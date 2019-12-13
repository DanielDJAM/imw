from fabric.api import env, cd, local, run

# nombre de la máquina de producción
env.hosts = ['vm.alu6393.me']

def deploy():
    local('git push')
    with cd('~/webapps/vmweb'):
      run('git pull')
    run('supervisorctl restart vmweb')
