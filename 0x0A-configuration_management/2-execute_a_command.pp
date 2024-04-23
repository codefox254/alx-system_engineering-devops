exec { 'killmenow_process':
  command => '/usr/bin/pkill killmenow',
  unless  => '/usr/bin/pgrep -f killmenow',
  returns => [0, 1],
}
