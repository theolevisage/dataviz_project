apt update -y
which gpg || apt install gpg -y
mkdir /.keys
FILE=/.keys/public.pgp
if test -f "$FILE"; then
    echo "$FILE exists."
else
    echo "$FILE does not exist."
    gpg --batch --gen-key keygen-batch
    gpg --output /.keys/public.pgp --armor --export mail@example.com
fi