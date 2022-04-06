which gpg || apt install gpg
gpg --batch --gen-key keygen-batch
gpg --output public.pgp --armor --export name@email.com