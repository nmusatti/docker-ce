#/bin/bash

echo '{
  "storage-driver": "overlay2"
}' | sudo tee /etc/docker/daemon.json
