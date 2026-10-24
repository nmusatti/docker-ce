import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# The test containers can't run a Docker daemon, so only the installation
# is checked.

def test_docker_packages(host):
    for p in ('docker-ce', 'docker-ce-cli', 'containerd.io',
              'docker-buildx-plugin', 'docker-compose-plugin'):
        assert host.package(p).is_installed


def test_docker_cli(host):
    assert host.run('docker --version').rc == 0
    assert host.run('docker compose version').rc == 0


def test_docker_group(host):
    assert host.group('docker').exists


def test_no_old_apt_source(host):
    if host.system_info.distribution == 'ubuntu':
        assert not host.file('/etc/apt/sources.list.d/docker.list').exists
        assert host.file('/etc/apt/sources.list.d/docker.sources').exists
