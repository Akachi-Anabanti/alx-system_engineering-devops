#!/usr/bin/env bash
# A file that installs and configures nginx on ubuntu
# Install nginx
package { 'nginx':
  ensure => installed,
}

# create the root directory
file { 'etc/nginx/html':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# create the index.html file
file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# configure the default
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
         listen 80;
         listen [::]:80 default_server;
         root /etc/nginx/html;
         index  index.html index.htm;

          location /redirect_me {
            return 301 https://anabanti-akachi.github.io/;
          }
        }"
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# enable and restart the nginx service

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
      Package['nginx'],
      File['/etc/nginx/html'],
      File['/etc/nginx/html/index.html'],
      File['/etc/nginx/sites-available/default'],
    ],
}
