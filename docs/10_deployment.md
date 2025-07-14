# Deployment

## jenkins
* freestyle
* pipeline

### plugins required
* python
* envinject
* allure

### env variables

1. global properties

2. using Envinject plugin
   - Properties Content

3. environment (pipeline)
   - Use json pipeline config

## Build Steps
### Execute Shell

```shell
  python3.11 -V
  python3.11 -m venv venv
  . venv/bin/activate
  pip install -r requirements.txt
  python3.11 -m pytest todo_api/ -v -s --alluredir reports/allure/allure-results

```

```json
pipeline {
    agent any

    environment {
        VAR = 'value'
        VAR2    = 'value'
    }

    stages {
        stage('python version') {
            steps {
              sh 'python3 --version'
            }
        }
        stage('Run Python Scripts') {
            steps {
                withPythonEnv('python3') {
                    sh 'pip install -r requirements.txt'
                    sh 'python3 -m behave -f allure_behave.formatter:AllureFormatter -o allure-results'
                }
            }
        }
        stage('reports') {
            steps {
                script {
                    allure ([
                        includeProperties: false,
                        jdk:'',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                 }
            }
        }
    }
}

```

### Post build actions
- Allure Reports



## docker

> docker example

```yaml
# image with python
FROM python:3

# label del maintainer
LABEL maintainer="edwin.taquichiri@jalasoft.com"

# copy the code to /opt/app folder
COPY . /opt/app
WORKDIR /opt/app

# update system
RUN apt-get update

# install java always add -y option
RUN apt-get install -y default-jre
RUN java -version

# install allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb
RUN dpkg -i allure_2.18.1-1_all.deb

# install/upgrade pip
RUN python3 -m pip install --upgrade pip

# install virtualenv librarary/package
RUN python3 -m pip install --user virtualenv

# create virtualenv for the framework
RUN python3 -m venv env

# activate virtual environment
RUN . env/bin/activate

# install requirements
RUN python3 -m pip install -r requirements.txt
```
Deploy docker container

```shell
  docker build --tag 'name' .
```

Run docker image
```shell
  docker run -it <image name or id> bash
```

## GitLab

```yaml
image: python:3

stages:
  - lint
  - pytest

before_script:
  - python3 -m venv venv
  - source venv/bin/activate
  - pip install -r requirements.txt

pylint:
  stage: lint
  script:
    - echo "pylint"

test:
  stage: pytest
  script:
    - python3 -m pytest src/api/ -v -s

```
## Final Task

### Option 1
* Deploy your frameworks(TDD and BDD) on any CD/CI (jenkins, docker, gitlab)

### Option 2
* Create a Dashboard for your framework(TDD or BDD) using Grafana and influxdb


## Refs.

> jenkins https://www.jenkins.io/doc/book/installing/linux/

> jenkins pipeline https://www.jenkins.io/doc/pipeline/tour/hello-world/
