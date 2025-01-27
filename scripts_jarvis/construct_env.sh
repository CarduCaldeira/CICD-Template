!/bin/bash

UV_COMPILE_BYTECODE=1
export UV_COMPILE_BYTECODE

USERNAME="newuser"

USERNAME_DIR="/home/$USERNAME/"

useradd -M -s /bin/bash "$USERNAME"
mkdir $USERNAME_DIR
chmod -R 777 "$USERNAME_DIR"

mkdir /home/.local/bin

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

chmod -R 777 /home/.cache
chmod -R 777 /home/.local/share/

uv python install 3.12

mkdir $USERNAME/actions-runner && chmod -R 777 $USERNAME/actions-runner/ && cd $USERNAME/actions-runner

curl -o actions-runner-linux-x64-2.321.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.321.0/actions-runner-linux-x64-2.321.0.tar.gz
echo "***  actions-runner-linux-x64-2.321.0.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-linux-x64-2.321.0.tar.gz

su - "$USERNAME" -c "cd /home/$USERNAME/actions-runner && ./config.sh --url https://github.com/CarduCaldeira/CICD-Template --token **** && ./run.sh"
