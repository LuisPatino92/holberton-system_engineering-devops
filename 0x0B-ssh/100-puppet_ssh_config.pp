# Ensures that there is a holberton file in tmp
file_line { '/etc/ssh/ssh_config':
  ensure => 'present',
  line   => '	PasswordAuthentication no'
}
file_line { '/etc/ssh/ssh_config':
  ensure => 'present',
  line   => '	IdentityFile ~/.ssh/holberton'
}
