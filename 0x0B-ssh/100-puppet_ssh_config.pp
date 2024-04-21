# Puppet script to customize SSH configuration for passwordless server access
# by specifying a custom SSH private key and disabling password authentication.

include stdlib

file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}

# Explanation of the regular expression:
#
# ^       Start of the line
# [#]*    Zero or more hash characters
# [\s]*   Zero or more whitespace characters
# (?i)    Case-insensitive match
# IdentityFile  Exact match for "IdentityFile"
# [\s]+   One or more whitespace characters
# ~/.ssh/id_rsa   Exact match for the default SSH private key path
# $       End of the line

file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}

# Explanation of the regular expression:
#
# ^       Start of the line
# [#]*    Zero or more hash characters
# [\s]*   Zero or more whitespace characters
# (?i)    Case-insensitive match
# PasswordAuthentication  Exact match for "PasswordAuthentication"
# [\s]+   One or more whitespace characters
# (yes|no)   Match either "yes" or "no"
# $       End of the line
