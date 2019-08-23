[![Build Status](https://cloud.drone.io/api/badges/gcavalcante8808/labels2env/status.svg)](https://cloud.drone.io/gcavalcante8808/labels2env)

### Labels2Env

Utility to dump and export Github Pull Requests Labels to environment variables.

### How to use

Download the utility from releases page and mark it as a executable.

The program have the following syntax:

```bash
    ./labels2env --github-token <GITHUB_TOKEN> \
                 --github-repo <GITHUB_REPO> \
                 --github-pr-number <GITHUB_PR_NUMBER> \
                 --github-label-pattern <GITHUB_LABEL_PATTERN> \
                 --github-label-separator-pattern <GITHUB_LABEL_SEPARATOR_PATTERN>
```

To use it, you need to provide the following params:


 * GITHUB_TOKEN: A personal github token with `repo` privileges.
 * GITHUB_REPO: The base reposity where pull requests to read in the format "user/repo";
 * GITHUB_PR_NUMBER: The number of the pull request where the labels will be read;
 * GITHUB_LABEL_PATTERN: The pattern that will be matched to filter labels.
 * GITHUB_LABEL_SEPARATOR_PATTERN: Pattern that will be used to split the label.

After providing the needed info (see the example below), the utility will read labels from a specific pull request and dump all labels
that match the pattern provided in `GITHUB_LABEL_PATTERN`, spliting key and value based on `GITHUB_LABEL_SEPARATOR_PATTERN`.

### Example 

Consider the following scenario:

 - A Pull Request with 'CI:RESOURCE1', 'CI:RESOURCE2', 'OTHER', 'BUG' labels;
 - Labels2env invoked with `GITHUB_LABEL_PATTERN=CI` and `GITHUB_LABEL_SEPARATOR_PATTERN=:`

 With the above statements, when you run the labels2env:
 
 ```
     ./labels2env --github-token mytoken \
                 --github-repo myuser/myrepo \
                 --github-pull 10533 \
                 --github-label-pattern CI \
                 --github-label-separator-pattern :
```

You will get in return:

```
    RESOURCE1=1
    RESOURCE2=1
```

Note that other labels ('BUG','OTHER', etc) will not be pulled into the vars because they dont fit in the filters.
You can even export the result directly using an eval statement:

 ```
     eval $(./labels2env --github-token mytoken \
                 --github-repo myuser/myrepo \
                 --github-pull 10533 \
                 --github-label-pattern CI \
                 --github-label-separator-pattern :)
```

**But beware; specially crafted labels can lead eval into security treats.**


### Other

**You can choose to pass the arguments directly to utility like the examples above or you can use environment
variables with same names (GITHUB_TOKEN, GITHUB_REPO, GITHUB_PR_NUMBER, GITHUB_LABEL_PATTERN, GITHUB_LABEL_SEPARATOR_PATTERN)
to provide the required info.**