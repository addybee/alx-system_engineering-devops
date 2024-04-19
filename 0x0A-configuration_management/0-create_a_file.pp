#create a file in /tmp.

file{ '/tmp/school':
  ensure  => present                #create a file in /tmp/school if absent.
  path    => '/tmp/school'            #File path is /tmp/school
  mode    => '0744'                   #File permission is 0744
  owner   => 'www-data'               #File owner is www-data
  group   => 'www-data'               #File group is www-data
  content => 'I love Puppet'          #File contains I love Puppet
}
