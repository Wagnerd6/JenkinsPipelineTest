/* Requires the Docker Pipeline plugin */ 
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                bat 'echo "The pipeline is running xoxoxo"'
                bat 'python --version'
            }
        }
    }
}
