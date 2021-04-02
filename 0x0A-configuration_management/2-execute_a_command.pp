#Kills a proccess called killmenow if it is active
exec {'kill_killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin/', '/bin'],
}
