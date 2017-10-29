## Django server deployment + email server on Linux
The purpose of this document is to serve as a reference log to the setup process that I will be undergoing to install and set up mod_WSGI, Postfix and Dovecot on Debian Linux.  
Hopefully this document will allow me and others to get started quicker when doing this next time.

### Preparation
For this setup I will be needing a few packages.  
These are:
+ Dovecot
+ Postfix
+ mod_WSGI (make needed)
+ python3
+ Django
+ Apache web server
+ pip
+ mod_wsgi-express (with `pip install mod_wsgi`)

### Email setup

### Python and Django
Installed `Django`, `python-social-auth`, `social-auth-app-django`.  


### mod_WSGI
Used letsencrypt tutorial:  
`$ sudo apt-get install python-certbot-apache`
and  
`$ sudo certbot`
to install certificate.

After installing with pip, I used:
`$ python3 manage.py runmodwsgi --setup-only --port=80 --user=www-data --group=www-data --server-root=/srv/mod_wsgi-express-80 --https-only --https-port=443 --ssl-certificate-file=/letsencrypt/live/itgmarket.se/cert.pem --ssl-certificate-key-file=/letsencrypt/live/itgmarket.se/key.pem --server-name=itgmarket.se
`  
To configure the mod_wsgi-express server.  
Then it could be run with `$ sudo /srv/mod_wsgi-express/apachectl start`
