class ssh::config {
  file { ssh::params::ssh_service_config:
    PasswordAuthentication => No
    StricHostKeyChecking => No
  }
}
