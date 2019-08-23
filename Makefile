SHELL = /bin/bash
.SHELLFLAGS = -euox pipefail -c
.RECIPEPREFIX +=
.PHONY: test test-ci

test:
    coverage run --source=./labels2env -m pytest labels2env/tests.py
    coverage html

test-ci: test
    codecov --token=$${CODECOV_TOKEN} --commit=${COMMIT_SHA}

release: clear build_and_test_release_binaries
    cd src
    ghr -replace v1.0.0 dist/


.ONESHELL: build_and_test_release_binaries
build_and_test_release_binaries:
    cd labels2env
    pyinstaller -F labels2env.py
    dist/labels2env --help

clear:
    cd labels2env
    rm -rf dist/ build/
