
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
                sh 'docker run --rm -v "$WORKSPACE:/app" -w /app python:3.12-slim python factorial.py 5'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t factorial-app .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images factorial-app'
            }
        }
    }
}

