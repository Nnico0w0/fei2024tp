#!/bin/bash

if docker-compose ps | grep -q "django"; then
    docker-compose exec django /bin/bash
else
    echo "El servicio de Django no está en ejecución."
fi

