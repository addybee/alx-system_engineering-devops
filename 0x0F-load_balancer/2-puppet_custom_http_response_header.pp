# configure a server
$add_header = 'sudo sed -i "/listen 80 default_server;/,/location \/ {/ { /location/a\\
        add_header X-Served-By \"$HOSTNAME\";
}" /etc/nginx/sites-available/default'

$conf = 'sudo sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://devhints.io/bash permanent;\\
    error_page 404 /404.html;\\
    location = /404.html {\\
        root /usr/share/nginx/html;\\
        internal;\\
    }\n" /etc/nginx/sites-available/default'

exec { 'update':
  command => 'sudo apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
package{ 'nginx':
    ensure    => latest,
    provider  => 'apt',
    before    => Exec['update'],
}

file{ 'index_file':
  path  => '/var/www/html/index.html'
  ensure  => file
  content => "Hello World!"
  before  => package['nginx']
}

exec{ 'custom_header':
  command => "${add_header}"
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  before  => File['index_file']
}

exec{ 'config':
  command => "${conf}"
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  before  => File['custom_header']
}
exec { 'restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/',
  before => File_line['config']
}
