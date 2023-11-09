#!/usr/bin/env bash
# seetting up webservers for Airbnb_clone_v2

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" >> /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo sed -i "41i \\\\tlocation /hbnb_static/ {\n\t\talias $link_file/;\n\t\tautoindex off;\n\t}\n" "$config"
sudo service nginx restart
