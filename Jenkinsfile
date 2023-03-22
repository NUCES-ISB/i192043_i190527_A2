pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                // Clone your GitHub repository
                git branch: 'main', credentialsId: 'dockerhub-credentials', url: 'https://github.com/NUCES-ISB/i192043_i190527_A2'
            }
        }
        stage('Build image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in your repository
                    app = docker.build("nasirabdullahsyed/btc-pricepredictor:latest")
                }
            }
        }
        stage('Push image') {
            steps {
                script {
                    // Log in to Docker Hub using your credentials
                    withDockerRegistry(credentialsId: 'dockerhub-credentials') {
                        // Push the Docker image to Docker Hub
                        app.push()
                    }
                }
            }
        }
        stage('Run') {
            steps {
                sh 'docker stop btc-pricepredictor || true'
                sh 'docker rm btc-pricepredictor || true'
                sh 'docker run -d --name btc-pricepredictor -p 5000:5000 nasirabdullahsyed/btc-pricepredictor:latest'
            }
        }
    }
}
