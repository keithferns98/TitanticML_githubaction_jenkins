pipeline{
    agent any
    environment{
        IMAGE = "keithfernandes/titanic-api:latest"
        CONTAINER = "titanic-api2"
        PORT = "8000"
    }
    stages{
        stage("Pull Docker Image."){
            steps{
                bat 'docker pull %IMAGE%'
            }
        }
        stage("Stop Existing Container"){
            steps{
                sh '''
                docker stop %CONTAINER% || true
                docker rm %CONTAINER% || true
                '''
            }
        }
        stage("Run Container"){
            steps{
                sh '''
                docker run -d \
                -p %PORT%:%PORT% \
                --name %CONTAINER% \
                %IMAGE%
                '''
            }
        }
    }
}