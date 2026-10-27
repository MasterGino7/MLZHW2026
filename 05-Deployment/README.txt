CÓDIGO UTILIZADO EN CONSOLA PARA LA TAREA
cd ./05-Deployment
uv sync --locked
uv run python smoke_test.py
sha256sum pipeline.bin


#Este debe ser el resultado de la linea anterior
1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1  pipeline.bin

uv run uvicorn predict:app --host 0.0.0.0 --port 9696


docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5

python q6_test.py