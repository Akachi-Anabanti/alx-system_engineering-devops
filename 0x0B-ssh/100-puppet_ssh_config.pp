# puppet manifest to configure SSH client

file {'/etc/ssh/ssh_config':
  ensure   => present,
  owner    => 'root',
  group    => 'root',
  mode     => '0644',
  content => "# SSH client Configurations\n
              Host *\n
              PasswordAuthentication no\n
              IdentityFile ~/.ssh/school\n",
}
