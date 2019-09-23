#!/bin/bash
# Also edit nginx/Dockerfile when changing project name!

if [ -z $1 ] || [ ! -f "./docker-compose.$2.yml" ]; then
    echo "!! Specify [config] and [command] !!";
    print_usage;
fi

if [ "$1" == "run" ] && [ -f "./$3/Dockerfile" ]; then
    CMD=$1;shift;CONF=$1;shift;SERVICE=$1;shift;
    docker-compose -f docker-compose.$CONF.yml $CMD --rm --service-ports --name $SERVICE $SERVICE "${@:-bash}";
elif [ "$1" == "build" ] || [ "$1" == "up" ] || [ "$1" == "push" ] || [ "$1" == "config" ]; then
    CMD=$1;shift;CONF=$1;shift;SERVICE=$1;shift;
    docker-compose -f docker-compose.$CONF.yml $CMD ${SERVICE:-};
else
    print_usage;
fi
