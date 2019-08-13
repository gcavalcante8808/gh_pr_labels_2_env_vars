from collections import namedtuple

from dump_gh_pull_labels.dump_github_labels_as_env_vars import get_supported_labels

gh_label_interface = namedtuple('Label', 'name')


def test_get_supported_labels_when_good_supported_labels_are_passed_and_return_clean_labels():

    github_labels = [gh_label_interface(name='CI:LABEL1'),
                     gh_label_interface(name='CI:LABEL2'),
                     gh_label_interface(name='CI:LABEL3')]
    github_label_pattern = 'CI'
    github_label_separator_pattern = ':'

    result = list(get_supported_labels(github_labels, github_label_pattern, github_label_separator_pattern))

    assert len(result) == 3
    assert 'LABEL1' in result
    assert 'LABEL2' in result
    assert 'LABEL3' in result
    assert 'CI' not in result
    assert ':' not in result
