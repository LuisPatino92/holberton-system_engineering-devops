#Ensures that there is a holberton file in tmp
file {'/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0600',
  content =>
  "# Read more about SSH config files: https://linux.die.net/man/5/ssh_config\nHost LuchoServer
  HostName 35.196.27.222
  User ubuntu
  Port 22
  IdentityFile ~/.ssh/holberton
  PasswordAuthentication no
",
}
