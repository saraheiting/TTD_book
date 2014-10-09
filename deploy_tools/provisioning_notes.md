Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

	sudo apt-get install nginx git python3-pip
	sudo pip install virtualenv

## First use fab to deploy
	(pg. 163)

	tech1-49s:deploy_tools sarah$ fab deploy:host=sarah@superlists-staging.saraheiting.com

## Nginx Virtual Host config

* see nginx.template.conf

* replace SITENAME with, eg, staging.my-domain.com
	(see pg. 165)

	sarah@superlists:~/sites/superlists.saraheiting.com/source$ sed "s/SITENAME/superlists.saraheiting.com/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/superlists.saraheiting.com

	sarah@superlists:~/sites/superlists.saraheiting.com/source$ sudo ln -s ../sites-available/superlists.saraheiting.com /etc/nginx/sites-enabled/superlists.saraheiting.com

## Upstart Job

* see gunicorn-upstart.template.conf

* replace SITENAME with, eg, staging.my-domain.com
	(pg. 165)

	sed "s/SITENAME/superlists.saraheiting.com/g" deploy_tools/gunicorn-upstart.template.conf | sudo tee /etc/init/gunicorn-superlists.saraheiting.com.conf

## Start nginx and gunicorn

	sarah@superlists:~/sites/superlists.saraheiting.com/source$ sudo service nginx reload

	sarah@superlists:~/sites/superlists.saraheiting.com/source$ sudo start gunicorn-superlists.saraheiting.com
	
## Folder structure
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv



