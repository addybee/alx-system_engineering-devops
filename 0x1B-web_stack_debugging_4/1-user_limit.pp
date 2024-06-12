# Fixes a user's number of open file limits
exec { 'update_hard_limit':
  command  => 'sed -i "s/^holberton.*hard.*nofile.*/holberton hard nofile 65536/" /etc/security/limits.conf',
  provider => shell,
  path     => ['/usr/bin', '/usr/sbin', '/bin'],
  before   => Exec['update_soft_limit'],
}

exec { 'update_soft_limit':
  command  => 'sed -i "s/^holberton.*soft.*nofile.*/holberton soft nofile 65536/" /etc/security/limits.conf',
  provider => shell,
  path     => ['/usr/bin', '/usr/sbin', '/bin'],
}
