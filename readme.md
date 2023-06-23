
## Login DefaultPW
#### rh_demo/demo
#### Create Command
#### echo -n ‘test-test’ | md5sum

## Build
#### podman build -t troble-pr .
## Run
#### podman run -d --name test -p 8032:8032 localhost/troble-pr
#### podman exec -it test /bin/bash

## Container image
#### podman pull quay.io/rhn_consulting_kemori/trouble-producer
#### podman run -d --name test -p 8032:8032 quay.io/rhn_consulting_kemori/trouble-producer