#create a file in /tmp.

file{ '/tmp/school':
  ensure  => file,                #create a file in /tmp/school if absent.
  path    => '/tmp/school'            #File path is /tmp/school
  owner   => 'www-data',               #File owner is www-data
  group   => 'www-data',               #File group is www-data
  mode    => '0744',                   #File permission is 0744
  content => 'I love Puppet',          #File contains I love Puppet
}
