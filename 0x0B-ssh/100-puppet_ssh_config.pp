# Puppet manifest to configure SSH client for passwordless authentication

# Ensure SSH directory exists
file { '/etc/ssh':
  ensure => directory,
}

# Configure SSH client to use private key for authentication
file_line { 'Declare identity file':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^(\s*)IdentityFile\s.*',
  append_on_no_match => true,
}

# Configure SSH client to refuse password authentication
file_line { 'Turn off passwd auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^(\s*)PasswordAuthentication\s.*',
  append_on_no_match => true,
}

# Notify SSH service to reload configuration
service { 'ssh':
  ensure  => running,
  enable  => true,
  require => File['/etc/ssh/ssh_config'],
}
