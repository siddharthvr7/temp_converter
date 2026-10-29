pipeline {
    agent any

    environment {
        IMAGE_TAG        = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
        DOCKER_IMAGE     = "siddharthvr7/temp-converter:${IMAGE_TAG}"
        DOCKER_REGISTRY  = "siddharthvr7/temp-converter"
    }

    stages {

        stage('Continuous Integration: Test') {
            steps {
                echo 'Checking dependencies and running automated unit tests...'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Build & Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USER', passwordVariable: 'TOKEN')]) {
                    echo 'Building Docker container image...'
                    bat "docker build -t ${DOCKER_IMAGE} ."
                    
                    echo 'Logging into Docker Hub...'
                    bat "docker login -u ${USER} -p ${TOKEN}"
                    
                    echo 'Pushing image to registry...'
                    bat "docker push ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Deployment to Kubernetes') {
            steps {
                echo 'Injecting unique tag and deploying to local Kubernetes cluster...'
                bat "powershell -Command \"(Get-Content k8s/deployment.yaml) -replace 'IMAGE_PLACEHOLDER', '${DOCKER_IMAGE}' | Set-Content k8s/deployment.yaml\""
                
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
                
                echo 'Verifying live Kubernetes resource allocations:'
                bat 'kubectl get pods'
                bat 'kubectl get service temp-converter-service'
            }
        }
    }
}
