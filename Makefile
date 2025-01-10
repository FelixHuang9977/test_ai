all:
	
setup:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt --no-index --find-links wheelhouse
	chmod +x ./diag_cli
	./diag_cli list

download_wheel:
	mkdir -p wheelhouse
	pip download -r requirements.txt -d wheelhouse

setup_online:
	venv/bin/pip install -r requirements.txt
	chmod +x ./diag_cli

release:
	pip freeze > requirements.txt
	mkdir -p wheelhouse
	pip download -r requirements.txt -d wheelhouse

clean:
	-rm -rf venv
	-rm -rf wheelhouse
	-find ./ -type d -name __pycache__ -exec rm -rf {} \;
	-find ./ -type d -name .pytest_cache -exec rm -rf {} \;