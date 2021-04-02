#installs puppet-lint in its 2.1.1 version
package {'puppet-lint':
  name            => 'puppet-lint',
  ensure          => installed,
  install_options => ['-v', '2.1.1'],
}
