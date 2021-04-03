#Ensures that there is a holberton file in tmp
file {'/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0600',
  content => '# Read more about SSH config files: https://linux.die.net/man/5/ssh_config\nHost LuchoServer\n\tHostName 35.196.27.222\n\tUser ubuntu\n\tPort 22\n\tIdentityFile ~/.ssh/holberton\n\tPasswordAuthentication no\n',
}
