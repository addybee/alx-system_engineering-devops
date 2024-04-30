# configure a server
$conf = "\tadd_header X-Served-By ${HOSTNAME};\n\t\\
rewrite ^/redirect_me https://devhints.io/bash permanent;\n\t\\
error_page 404 /404.html;\n\t\\
location = /404.html {\n\t\t\\
root /usr/share/nginx/html;\n\t\t\\
internal;}\n"
exec { 'update':
  command => 'sudo apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
package{'nginx':
    ensure    => latest,
    provider  => 'apt',
    before    => Exec['update'],
}

file{'index_file'
  path  => '/var/www/html/index.html'
  ensure  => file
  content => "Hello World!"
  before  => package['nginx']
}
file_line { 'custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => "${conf};",
  after   => 'listen 80 default_server;',
  before  => File['index_file']
}
exec { 'restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/',
  before => File_line['custom_header']
}
