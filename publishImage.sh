#!/bin/bash
############################################
# this script function is :
# deploy new docker container
#
# USER        YYYY-MM-DD - ACTION
# zhoutao    2019-06-13 - CREATED
# 使用加密工具包打镜像
############################################

parasnum=8
# function
help_msg()
{
cat << help
+----------------------------------------------------+
+ Error Cause:
+ you enter $# parameters
+ the total paramenter number must be $parasnum
+ 1st :DOCKER_NAME
+ 2nd :MODULE_NAME
+ 3rd :PROJECT_VERSION
+ 4rd :IMAGE_TAG
+ 5th :USERNAME
+ 6th :PASSWORD
+ 7th :DOCKER_REGISTRY_URL
+ 8th :DOCKER_REGISTRY
+----------------------------------------------------+
help
}

# ----------------------------------------------------
# Check parameter number
# ----------------------------------------------------
if [ $# -ne ${parasnum} ]
then
        help_msg
        exit
fi

# ----------------------------------------------------
# Initialize the parameter.
# ----------------------------------------------------
DOCKER_NAME=$1
MODULE_NAME=$2
PROJECT_VERSION=$3
IMAGE_TAG=$4
USERNAME=$5
PASSWORD=$6
DOCKER_REGISTRY_URL=$7
DOCKER_REGISTRY=$8

PROJECT_VERSION=${PROJECT_VERSION/"origin/"/""}

DOCKER_FILE="Dockerfile"


# ----------------------------------------------------
# check docker images
# ----------------------------------------------------
DOCKER_IMAGE=`docker images | grep ${DOCKER_NAME} | awk -F ' ' '{print $3}'`
if [ -n "${DOCKER_IMAGE}" ]; then

        # delete while docker image was exists
        echo "##Delete exists Image: "${DOCKER_IMAGE}
        docker rmi ${DOCKER_IMAGE}
fi
echo ""



# ----------------------------------------------------
# Init violet.key
# ----------------------------------------------------
echo "**Init violet start"
echo "password: TzVexRt7MSvLtJvZk2zWn6fwncBvjPzo" > violet.key
echo "algorithm: AES" >> violet.key
echo "keysize: 128" >> violet.key
echo "ivsize: 128" >> violet.key
echo "hold: HOLD" >> violet.key
echo "**Init violet end."



# ----------------------------------------------------
# Init dockerfile
# ----------------------------------------------------
echo "**Init dockerfile start: "${DOCKER_FILE}
echo "FROM openjdk:8u212" > ${DOCKER_FILE}
echo "VOLUME /tmp" >> ${DOCKER_FILE}
echo 'MAINTAINER zhoutao "zhout@chinaliancheng.com"' >> ${DOCKER_FILE}
#echo 'ENV LANG="en_US.UTF-8"' >> ${DOCKER_FILE}
echo 'ENV LANG="C.UTF-8"' >> ${DOCKER_FILE}
#echo 'ENV LANGUAGE="en_US:en"' >> ${DOCKER_FILE}
#echo 'ENV LC_ALL="en_US.UTF-8"' >> ${DOCKER_FILE}
echo "COPY violet.key  /usr/lsmsp/violet.key" >> ${DOCKER_FILE}
echo "COPY ${MODULE_NAME}-${PROJECT_VERSION}-final.jar  /home/avatar/data/dockerfiles/${DOCKER_NAME}/${MODULE_NAME}-${PROJECT_VERSION}-final.jar" >> ${DOCKER_FILE}
echo "RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone" >>${DOCKER_FILE}
echo "RUN sh -c 'touch /home/avatar/data/dockerfiles/${DOCKER_NAME}/${MODULE_NAME}-${PROJECT_VERSION}-final.jar'" >> ${DOCKER_FILE}
echo "CMD java -jar /home/avatar/data/dockerfiles/${DOCKER_NAME}/${MODULE_NAME}-${PROJECT_VERSION}-final.jar --violet.keyfile=/usr/lsmsp/violet.key" >> ${DOCKER_FILE}
cat ${DOCKER_FILE}
echo "**Init dockerfile end."

# ----------------------------------------------------
# Build dockerfile
# ----------------------------------------------------
echo ""
echo "##Build dockerfile for "${DOCKER_NAME}
docker build -t ${DOCKER_REGISTRY_URL}/${DOCKER_REGISTRY}/${DOCKER_NAME}:${IMAGE_TAG} .



# ----------------------------------------------------
# publish image
# ----------------------------------------------------
echo ""
echo "##publishing image : "${DOCKER_NAME}
docker login -u${USERNAME} -p${PASSWORD} ${DOCKER_REGISTRY_URL}
docker push ${DOCKER_REGISTRY_URL}/${DOCKER_REGISTRY}/${DOCKER_NAME}:${IMAGE_TAG}
docker logout ${DOCKER_REGISTRY_URL}

echo ""
# ----------------------------------------------------
# delete jar 、dockerfile and  sh
# ----------------------------------------------------
rm -rf *.jar
rm Dockerfile
rm violet.key
rm "$0"
