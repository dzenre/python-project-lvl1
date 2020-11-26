install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

package-install:
	pip install --user dist/*.whl

package-upgrade:
	pip install --upgrade dist/*.whl

lint:
	poetry run flake8 brain_games
