#puppet advance
exec { 'update':
  command  => 'sudo apt-get update',

}
-> package {'nginx':
  ensure => present,
}
-> file_line { 'header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  a_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}
-> exec { 'start':
  command  => 'sudo service nginx start',

}