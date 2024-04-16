# Increase user hard and soft limits

exec {'increase-user-hard-limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec {'increase-user-soft-limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 10240/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
