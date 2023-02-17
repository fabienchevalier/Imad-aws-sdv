pipeline {
    agent any
    stages {
        stage('Build and Test') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/fabienchevalier/fabien-aws-sdv.git']]])
                sh 'python -m pip install --upgrade pip && pip install requests'
                sh 'docker-compose up -d'
                sh 'sleep 10 && python uni_test.py'
            }
        }
        stage('Deploy to PPRD') {
            when {
                branch 'master'
            }
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs:
