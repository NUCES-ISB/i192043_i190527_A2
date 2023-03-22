pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                // Clone your GitHub repository
                git branch: 'hunaid-branch', credentialsId: 'dockerhub-credentials', url: 'https://github.com/NUCES-ISB/i192043_i190527_A2'
            }
        }
        stage('Build image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in your repository
                    app = docker.build("hunaid2000/btc-prediction:latest")
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
                sh 'docker stop btc-prediction || true'
                sh 'docker rm btc-prediction || true'
                sh 'docker run -d --name btc-prediction -p 5000:5000 hunaid2000/btc-prediction:latest'
            }
        }
    }
}
