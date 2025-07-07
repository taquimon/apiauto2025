pipeline {
    agent any

    environment {
        TOKEN_TODO = '9463fd6e63c3ac3e06372045795ef48264968d2c'
        URL_BASE = 'https://api.todoist.com/api/v1/'
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
                    sh 'python3 -m pytest src/api -vs'
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
