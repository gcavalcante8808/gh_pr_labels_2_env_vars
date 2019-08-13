SHELL = /bin/bash
.SHELLFLAGS = -euox pipefail -c
.RECIPEPREFIX +=
.PHONY: test test-ci

test:
    coverage run --source=./src -m pytest src/tests/
    coverage html

release: clear build_and_test_release_binaries
    cd src
    ghr -replace v1.0.0 dist/


.ONESHELL: build_and_test_release_binaries
build_and_test_release_binaries:
    cd dump_gh_pull_labels
    pyinstaller -F dump_github_labels_as_env_vars.py
    dist/dump_github_labels_as_env_vars --help

clear:
    cd dump_gh_pull_labels
    rm -rf dist/ build/
