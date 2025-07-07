pipeline {
    agent any

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
                    sh 'python3 -m pytest src/api -vs --alluredir reports/allure/allure-results --md-report --md-report-output md_report.md'
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
                        results: [[path: 'reports/allure/allure-results']]
                    ])
                 }
            }
        }
        stage('Send Report to Teams') {
            steps {
                withPythonEnv('python3') {
                    sh 'python3 web_hook.py'
                }
            }
        }
    }
}
