pipeline{
    agent any
    environment{
        IMAGE = "keith311/titanic-api:latest"
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
                bat '''
                docker stop %CONTAINER% 2>nul
                docker rm %CONTAINER% 2>nul
                '''
            }
        }
        stage("Run Container"){
            steps{
                bat '''
                docker run -d ^
                -p %PORT%:%PORT% ^
                --name %CONTAINER% ^
                %IMAGE%
                '''
            }
        }
    }
}