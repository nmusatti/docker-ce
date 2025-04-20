Ansible role: docker-ce
=======================

![test](https://github.com/nmusatti/docker-ce/actions/workflows/test.yml/badge.svg)

An Ansible role to install the official Docker Community Edition engine.
Supported distributions are the currently maintained releases of the Red Hat
family and derivatives, and Ubuntu LTS. At this time tests are run on Rocky Linux 9, 
CentOS Stream 10, CentOS Stream 9, Fedora 42, Fedora 41, Fedora 40,
Ubuntu 24.04 and Ubuntu 22.04.

Requirements
------------

None.

Role Variables
--------------

The variables that control the role behaviour are listed below with their respective defaults:

    start_service: True

Whether the docker system service should be started after installation.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: nmusatti.docker_ce

Note the underscore in the name.

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - https://github.com/nmusatti
