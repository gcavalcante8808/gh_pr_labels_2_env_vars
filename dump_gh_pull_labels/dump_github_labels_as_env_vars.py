# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from github import Github, Label

import os
import argparse

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', False)
GITHUB_REPO = os.getenv('GITHUB_REPO', False)
GITHUB_PULL = int(os.getenv('GITHUB_PULL', False))
GITHUB_LABEL_PATTERN = os.getenv('GITHUB_LABEL_PATTERN', 'CI')
GITHUB_LABEL_SEPARATOR_PATTERN = os.getenv('GITHUB_LABEL_SEPARATOR_PATTERN', ':')


def get_github_pr_labels(github_token, github_repo, github_pull):
    github_client = Github(github_token)
    repo = github_client.get_repo(github_repo)

    return repo.get_pull(github_pull)


def print_supported_labels_as_env_vars(supported_labels):
    for label in supported_labels:
        print('{}=1'.format(label))


def get_supported_labels(labels, label_pattern, label_separator):
    #  type: ([Label], str, str) -> [str]
    return [label.name.split(GITHUB_LABEL_SEPARATOR_PATTERN)[1] for label in labels if
            GITHUB_LABEL_PATTERN in label.name]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--github-token', type=str, required=True, default=GITHUB_TOKEN)
    parser.add_argument('--github-repo', type=str, required=True, default=GITHUB_REPO)
    parser.add_argument('--github-pull', type=int, required=True, default=GITHUB_PULL)
    parser.add_argument('--github-label-pattern', type=str, required=False, default=GITHUB_LABEL_PATTERN)
    parser.add_argument('--github-label-separator-pattern', type=str, required=False,
                        default=GITHUB_LABEL_SEPARATOR_PATTERN)

    args = parser.parse_args()

    github_labels = get_github_pr_labels(args.github_token, args.github_repo, args.github_pull)
    supported_labels = get_supported_labels(github_labels, args.github_label_pattern, args.github_label_separator_pattern)

    print_supported_labels_as_env_vars(supported_labels)
