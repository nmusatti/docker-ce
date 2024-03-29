Ansible role: docker-ce
=======================

![test](https://github.com/nmusatti/docker-ce/actions/workflows/test.yml/badge.svg)

An Ansible role to install the official Docker Community Edition engine.
Supported distributions are the currently maintained releases of the Red Hat
family and derivatives, and Ubuntu LTS.

Currently tests succeed on my Rocky Linux 8 developemnt machine for all distros 
provided I enable iptables in the running kernel. I'm currently trying to
address this problem within GitHub Actions. 

Requirements
------------

None.

Role Variables
--------------

The variables that control the role behaviour are listed below with their respective defaults:

    docker_compose_version: v2.2.2

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
