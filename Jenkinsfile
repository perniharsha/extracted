pipeline {
    agent any

    environment {
        // Docker Hub credentials
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_TAG = "perni007/python_backend:${BUILD_NUMBER}"
    }

    triggers {
        githubPush()  // Trigger build on GitHub push
    }

    stages {

        stage('Checkout') {
            steps {
                retry(3) {
                    git credentialsId: 'your-credential-id', branch: 'main', url: 'https://github.com/perniharsha/extracted.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_TAG} ."
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh "echo ${DOCKERHUB_PASSWORD} | docker login -u ${DOCKERHUB_USERNAME} --password-stdin"
                }
            }
        }

        stage("Push Docker Image") {
            steps {
                sh "docker push ${IMAGE_TAG}"
            }
        }

        stage("Deploy to Kubernetes") {
            steps {
                sh "kubectl set image deployment/pybackend container-0=${IMAGE_TAG} -n default"
                sh "kubectl rollout restart deploy pybackend -n default"
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}
