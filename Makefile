.EXPORT_ALL_VARIABLES:
LOG_PATH=docminer_logs.log
LOG_LEVEL_FILE=DEBUG
LOG_LEVEL_CONSOLE=DEBUG
LOG_FORMATTER_CONSOLE=console

app-run:
	python src/manager.py

tests-watch:
	ptw -- --cov-report term:skip-covered --cov=src --cov-config=.coveragerc tests

test-report:
	pytest --cov=src --cov-report html:cov_html tests