pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "siddharthvr7/temp-converter"
        // Injects standard Windows installations directories directly into the run path
        PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Docker\\Docker\\resources;${env.PATH}"
    }

    stages {
        stage('Initialize Pipeline Properties') {
            steps {
                script {
                    echo 'Generating unique tag fingerprints using Git...'
                    String rawTag = bat(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    String[] lines = rawTag.split('\n')
                    env.IMAGE_TAG = lines[lines.length - 1].trim()
                    
                    env.DOCKER_IMAGE = "siddharthvr7/temp-converter:${env.IMAGE_TAG}"
                    echo "Target build tag registered: ${env.DOCKER_IMAGE}"
                }
            }
        }

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
                    bat "docker build -t ${env.DOCKER_IMAGE} ."
                    
                    echo 'Logging into Docker Hub...'
                    bat "docker login -u ${USER} -p ${TOKEN}"
                    
                    echo 'Pushing image to registry...'
                    bat "docker push ${env.DOCKER_IMAGE}"
                }
            }
        }

        stage('Deployment to Kubernetes') {
            steps {
                echo 'Injecting unique tag and deploying to local Kubernetes cluster...'
                bat "powershell -Command \"(Get-Content k8s/deployment.yaml) -replace 'IMAGE_PLACEHOLDER', '${env.DOCKER_IMAGE}' | Set-Content k8s/deployment.yaml\""
                
                // Runs local deployment commands directly into your cluster architecture
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
                
                echo 'Verifying live Kubernetes resource allocations:'
                bat 'kubectl get pods'
                bat 'kubectl get service temp-converter-service'
            }
        }
    }
}
