# this manifest  kills a process named killmenow.

exec { 'pkill -f "./killmenow"':
  path   => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif => 'pgrep -f "./killmenow"',
}
