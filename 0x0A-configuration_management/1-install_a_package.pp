# A manifest for installing flask 2.1.0
# from pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
