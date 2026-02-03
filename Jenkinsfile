pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/harsh-sojitra-901/CICD'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t demo_cicd -f Dockerfile'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f flask-app || true
                docker run -d -p 5000:5000 --name jenkins_cicd demo_cicd:latest
                '''
            }
        }
    }
}
