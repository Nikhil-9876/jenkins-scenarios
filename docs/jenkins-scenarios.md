# Jenkins job setup

All three jobs use the same stages: build the image, run the tests in a clean
container, and start the deployed service on port 8000.

## Scenario 1 — local folder without Git

Create a Pipeline job and choose **Pipeline script**. Paste the contents of
`jenkins/scenario-1/Jenkinsfile` into the Pipeline definition. Before running
the job, define `LOCAL_PROJECT_PATH` as the absolute path to this folder, for
example `D:/Projects/jenkins-scenarios`. The job must run on a node labelled
`local` because `customWorkspace` is only available inside `node { ... }`.

This scenario is manual (or scheduled); Jenkins cannot detect changes in a
plain folder. The repository itself is not required for the job to work.

## Scenario 2 — local Git repository

Commit the project and Jenkinsfile to a local repository:

```text
git init
git add .
git commit -m "Initial Jenkins demo"
```

Create a Pipeline job with **Pipeline script from SCM**, **Git**, the local
repository URL (for example `file:///D:/Projects/jenkins-scenarios`), branch
`*/main`, and script path `jenkins/scenario-2/Jenkinsfile`. Keep the agent
label `local`. Enable Poll SCM if builds should follow local commits.

## Scenario 3 — GitHub repository

Push this repository and its Jenkinsfile to GitHub. Configure **Pipeline
script from SCM** with **Git**, the GitHub HTTPS URL, branch `*/main`, and
script path `jenkins/scenario-3/Jenkinsfile`. Use credentials for a private
repository. `agent any` is safe only when every eligible agent has Docker and
Compose; otherwise use a label such as `docker`.

For automatic builds, enable **GitHub hook trigger for GITScm polling** and
configure a webhook to a publicly reachable Jenkins URL. For localhost, use
Poll SCM instead.

## Linux agents

The supplied files use `bat` because the lab scenario uses Windows. On a Linux
agent, replace each `bat '...'` with `sh '...'` and use a POSIX path in the
scenario-1 `customWorkspace`.
