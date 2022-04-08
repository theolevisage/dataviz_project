apt update -y
which gpg || apt install gpg -y
mkdir /.keys
FILE=/.keys/public.pgp
if test -f "$FILE"; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    export name=$1
    export mail=$2
    envsubst < keygen-batch > updated-keygen-batch
    gpg --batch --gen-key updated-keygen-batch
    gpg --output /.keys/public.pgp --armor --export mail@example.com
fi