Ansible role: docker-ce
=======================

![test](https://github.com/nmusatti/docker-ce/actions/workflows/test.yml/badge.svg)

An Ansible role to install the official Docker Community Edition engine.
Supported distributions are the currently maintained releases of the Red Hat
family and derivatives, and Ubuntu LTS. At this time tests are run on Rocky Linux 10, Rocky Linux 9,
CentOS Stream 10, CentOS Stream 9, Fedora 44, Fedora 43, Ubuntu 26.04, Ubuntu 24.04 and
Ubuntu 22.04.

On Ubuntu the Docker repository is configured in `/etc/apt/sources.list.d/docker.sources`.
The `docker.list` file and the key in `/usr/share/keyrings` created by versions up to 1.3
are removed.

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

Testing
-------

The tests use Molecule with rootless Podman. Test images are built from
`molecule/Dockerfile.j2`, and the distributions are listed in `molecule/distros`.

    python3 -m venv .venv
    .venv/bin/pip install -r requirements-dev.txt
    PATH=$PWD/.venv/bin:$PATH scripts/molecule-matrix -d ubuntu2604   # or no -d for all

The test containers can't run the Docker daemon, so the tests check the installation only.

Releasing
---------

Pushing a tag `vX.Y.Z` on `master` runs the tests and, if they all pass, imports the role into
Galaxy. The import needs a Galaxy API token (https://galaxy.ansible.com/ui/token) stored as the
repository secret `GALAXY_API_KEY`.

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - https://github.com/nmusatti
