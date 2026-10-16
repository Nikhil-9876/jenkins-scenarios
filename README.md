# Jenkins CI/CD scenarios

This repository contains a small Flask application and three Jenkins pipeline
definitions for the same build → test → deploy workflow. The only difference
between the scenarios is where Jenkins obtains the source code.

## Prerequisites

- Jenkins LTS with the Pipeline and Git plugins
- A Jenkins agent with Docker Desktop and Docker Compose available on `PATH`
- The agent label `local` for scenarios 1 and 2

The examples target a Windows Jenkins agent because the original lab uses
`bat` steps. Replace `bat` with `sh` if the agent is Linux.

## Scenarios

| Scenario | Pipeline file | Jenkins job configuration |
|---|---|---|
| Local folder, no Git repository | [`jenkins/scenario-1/Jenkinsfile`](jenkins/scenario-1/Jenkinsfile) | Pipeline script; set `LOCAL_PROJECT_PATH` to the project folder |
| Local Git repository | [`jenkins/scenario-2/Jenkinsfile`](jenkins/scenario-2/Jenkinsfile) | Pipeline script from SCM; use a `file:///...` Git URL |
| GitHub repository | [`jenkins/scenario-3/Jenkinsfile`](jenkins/scenario-3/Jenkinsfile) | Pipeline script from SCM; use the HTTPS GitHub URL |

Detailed setup instructions are in [`docs/jenkins-scenarios.md`](docs/jenkins-scenarios.md).

## Run the application locally

```text
docker compose up --build -d
```

Open <http://localhost:8000>. To run the tests without Docker, install the
requirements and run `pytest`.
