# install flask from pip3.

exec { 'pip3 install Flask==2.1.0':
  path   => '/usr/bin:/usr/sbin:/bin',
  unless => '/usr/bin/pip3 show Flask | grep -q "^Version: 2.1.0$"',
}
