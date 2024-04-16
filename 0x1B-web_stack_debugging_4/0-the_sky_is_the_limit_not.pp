# Fixing the max file opened error by 

# increasing the ULIMIT in the default file

exec {'set-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/bin/local/bin/:/bin/'
}
# Restart
exec {'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d'
}
