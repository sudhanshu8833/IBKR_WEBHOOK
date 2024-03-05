#!/bin/bash
conda deactivate
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "${script_dir}/manage.py" runserver 4050 &
pid2=$!

ngrok http --domain=ibkrapp.ngrok.io 4050
wait $pid2

echo "COMPLETED"
