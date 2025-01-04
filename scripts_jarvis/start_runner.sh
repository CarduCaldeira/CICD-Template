#!/bin/bash

UV_COMPILE_BYTECODE=1
export UV_COMPILE_BYTECODE

USERNAME="newuser"

useradd -M -s /bin/bash "$USERNAME"
RUNNER_DIR="/home/$USERNAME/actions-runner"

if [ ! -f "$RUNNER_DIR/.runner" ]; then
    echo "Configurando o runner..."
    su - "$USERNAME" -c "cd $RUNNER_DIR && ./run.sh"
else
    echo "Runner já configurado. Iniciando..."
    su - "$USERNAME" -c "cd $RUNNER_DIR && ./run.sh"
fi

echo "Runner iniciado com sucesso."