apt update -y
which gpg || apt install gpg -y
mkdir /.keys
mkdir /batch
export NAME=$1
export MAIL=$2
envsubst < keygen-batch > /batch/updated-keygen-batch
gpg --batch --gen-key /batch/updated-keygen-batch