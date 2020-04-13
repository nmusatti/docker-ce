Ansible role: docker-ce
=======================

[![Build Status](https://travis-ci.org/nmusatti/docker-ce.svg?branch=master)](https://travis-ci.org/nmusatti/docker-ce)

An Ansible role to install the official Docker Community Edition. Currently only Red Hat distributions are supported,
i.e. CentOS 7, CentOS 8 and Fedora.


Requirements
------------

None.

Role Variables
--------------

The variables that control the role behaviour are listed below with their respective defaults:

    docker_compose_version: 1.25.5

The docker-compose release to be installed, as indicated on the [Releases page](https://github.com/docker/compose/releases) of the [docker-compose GitHub project](https://github.com/docker/compose).

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: nmusatti.docker_ce

Note the underscore in the name. Ansible Galaxy did not accept my submission otherwise.

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - https://github.com/nmusatti
