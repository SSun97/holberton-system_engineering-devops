# Puppt
class ssh::config {
  file { ssh::params::/etc/ssh/ssh_config:
    PasswordAuthentication => No
    StricHostKeyChecking => No
  }
}
