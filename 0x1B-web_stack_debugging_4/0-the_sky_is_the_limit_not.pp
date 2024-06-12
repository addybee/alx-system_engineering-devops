# Fixes requests failure by increasing the number of open file limit
exec { 'update_file_limit':
  command  => 'sed -i "s/^ULIMIT=.*/ULIMIT=\"-n 8000\"/" /etc/default/nginx',
  provider => shell,
  path     => ['/usr/bin', '/usr/sbin', '/bin'],
  notify   => Service['nginx'],
  unless   => 'grep -q "^ULIMIT=\"-n 8000\"" /etc/default/nginx',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Exec['update_file_limit'],
}
