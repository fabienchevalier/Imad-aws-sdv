pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/fabienchevalier/fabien-aws-sdv.git']]])
                sh 'python3 -m pip install --upgrade pip && pip3 install requests'
                sh 'sudo docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                sh 'sleep 10 && python3 uni_test.py'
            }
        }
    }
    post {
        always {
            sh 'sudo docker-compose down'
        }
    }
}