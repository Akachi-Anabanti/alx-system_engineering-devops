exec { 'kill_process':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
}
