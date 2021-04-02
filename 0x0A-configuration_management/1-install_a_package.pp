#installs puppet-lint in its 2.1.1 version
package {'puppet-lint':
  ensure          => installed,
  name            => 'puppet-lint',
  install_options => ['-v', '2.1.1'],
}
