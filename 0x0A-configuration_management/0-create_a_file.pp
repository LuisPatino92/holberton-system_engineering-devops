# Ensures that there is a holberton file in tmp

file {'/tmp/holberton':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love puppet',
}
