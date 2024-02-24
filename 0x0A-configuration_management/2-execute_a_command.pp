# A manifest that executes a kill command on
# process named 'killmenow'
exec { 'kill_process':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
}
