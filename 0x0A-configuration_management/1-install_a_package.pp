# Install Python package manager pip3
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install compatible version of Werkzeug
package { 'werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
