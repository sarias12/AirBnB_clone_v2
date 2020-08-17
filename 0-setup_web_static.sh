#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static.
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo -e '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>html tets</title>
</head>
<body>
    <h1>Holberton School test</h1>
</body>
</html>
' | sudo tee '/data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/pass the PHP/i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
