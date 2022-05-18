pipeline {
    agent {
        docker {'python:3.9'
        args '--user 0:0'}
    }
    stages {
        stage("build") {
            steps {
                echo 'building the application...'
            }
        }
        stage("test") {
            steps {
                echo 'testing the application...'
                sh 'pip install -U pytest --user'
                sh 'pip install -U -r requirements.txt --user'
                sh 'python -m pytest'
            }
        }
        stage("deploy") {
            steps {
                echo 'deploying the application...'
            }
        }
    }
    post {
        always {
            sh "echo POST-ACTION always"
        }
        cleanup {
            cleanWs()
        }
    }
}