#!/usr/bin/env bash
# This Script sets up your web servers for the deployment of web_static

# install nginx
sudo apt-get -y update
sudo apt-get install -y nginx

# Create folder if it doesn't exist
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create html file with content
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create a symbolic link to these directories
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# nginx configuration

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
