
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Factorial') {
            steps {
                sh 'python3 factorial.py 5'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t factorial-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run --rm factorial-app'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images factorial-app'
            }
        }
    }
}
