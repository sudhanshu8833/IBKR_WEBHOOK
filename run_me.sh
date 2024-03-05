#!/bin/bash
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "${script_dir}/env/bin/activate"
python3 "${script_dir}/app.py" &
pid2=$!

ngrok http --domain=smashing-helpful-mudfish.ngrok-free.app 4050
wait $pid2

echo "COMPLETED"
