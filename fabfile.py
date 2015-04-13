from fabric.api import env, local, cd, run, settings, sudo
from fabric.context_managers import prefix
import os


env.django_project_dir = '/home/mariusz/thumbs/thumbs/'
env.virtualenv_dir = '/home/mariusz/thumbs/v-env/'
env.activate = 'source ' + os.path.join(env.virtualenv_dir, 'bin/activate')


def create_virtualenv():
    sudo("pip install virtualenv")
    run("virtualenv " + env.virtualenv_dir)
    

def prepare_solr_thumbnail():
    '''
    Preparations for solr-thumbnail
    there are req for other dependecies
    '''
    
    """
    Pillow
    """
    sudo("apt-get install libjpeg62 libjpeg62-dev zlib1g-dev")
    
    """
    pgmagick
    """
    sudo("apt-get install libgraphicsmagick++-dev libboost-python-dev")
    
    """
    imagemagick
    """
    sudo("apt-get install imagemagick")
    
    """
    Wand
    """
    sudo("apt-get install libmagickwand-dev")


def deploy():
    """
    collect every requirements, test and run project
    """
    create_virtualenv()
    with cd(env.django_project_dir):
        prepare_solr_thumbnail()
        with prefix(env.activate):
            run("pip install -r req.txt")
            run("python ./manage.py test")
            run('python ./manage.py syncdb')
            run('python ./manage.py runserver')
        

