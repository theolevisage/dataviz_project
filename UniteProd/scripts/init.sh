apt update -y
which gpg || apt install gpg -y
mkdir /.keys
mkdir /batch
FILE=/.keys/public.pgp
if test -f "$FILE"; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    export NAME=$1
    export MAIL=$2
    envsubst < keygen-batch > /batch/updated-keygen-batch
    gpg --batch --gen-key /batch/updated-keygen-batch
    gpg --output /.keys/public.pgp --armor --export $2
fi