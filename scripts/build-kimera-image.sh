#!/bin/sh
git clone https://github.com/MIT-SPARK/Kimera-VIO.git
cd Kimera-VIO
docker build --rm -t zaba247/kimera-vio -f ./scripts/docker/Dockerfile .
# sudo docker tag kimera_vio zaba247/kimera-vio
docker push zaba247/kimera-vio
