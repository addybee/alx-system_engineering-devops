# set up your client SSH configuration file so that you can connect to a
# server without typing a password.

file{ '/etc/ssh/ssh_config':
  ensure  => present,
  mode    => '0644',
  content => "Host *
    PasswordAuthentication no
    tIdentityFile ~/.ssh/school
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes",
}
