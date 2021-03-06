install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_etl_ex.py

format:
	black *.py


lint:
	pylint --disable=R,C app.py

All: install lint test
