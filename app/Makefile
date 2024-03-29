.PHONY: migrate
migrate:
	poetry run python -m manage migrate


.PHONY: migrations
migrations:
	poetry run python -m manage makemigrations

.PHONY: startapp
startapp:
	@echo Se crea la app $(name)
	mkdir apps/$(name)
	poetry run python -m manage startapp $(name) apps/$(name)
# make startapp name=your_app_name

.PHONY: run-server
run-server:
	poetry run python -m manage runserver_plus 0.0.0.0:8000


.PHONY: run-dev
run-dev:
	poetry run python -m manage runserver_plus 0.0.0.0:8000  & sass --watch static_files/scss/main.scss:static/css/style.css

# .PHONY: superuser
# superuser:
# 	poetry run python -m manage createsuperuser

# .PHONY: update
# update: install migrate install-pre-commit

.PHONY: shell
shell:
	poetry run python -m manage shell_plus

# .PHONY: dbshell
# dbshell:
# 	poetry run python -m manage dbshell

# .PHONY: up-dependencies-only
# up-dependencies-only:
# 	test -f .env || touch .env
# 	docker compose -f docker-compose.dev.yml up --force-recreate db

# .PHONY: test
# test:
# 	poetry run python -m app.manage test