# File: 2-user_limit.pp

# Define a class to manage user-specific limits
class user_limits {

    # Define a function to set limits for a specific user
    define user_limit(
        $username,
        $soft_limit,
        $hard_limit
    ) {
        # Ensure limits are set in limits.conf
        file { "/etc/security/limits.d/${username}.conf":
            ensure  => present,
            content => "### Managed by Puppet ###\n${username} soft nofile ${soft_limit}\n${username} hard nofile ${hard_limit}\n",
            mode    => '0644',
            owner   => 'root',
            group   => 'root',
        }
    }

    # Apply limits for user 'holberton'
    user_limit { 'holberton':
        username   => 'holberton',
        soft_limit => 65535,  # Adjust as per your system requirements
        hard_limit => 65535,  # Adjust as per your system requirements
    }

    # Notify to restart affected services if any
    notify { 'restart_puppet_services':
        message => 'Limits updated, services may need restart.',
        require => File["/etc/security/limits.d/holberton.conf"],
    }
}

# Include the class to apply the configuration
include user_limits

