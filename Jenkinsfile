pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '코드를 가져옵니다'
                checkout scm
            }
        }

        stage('Setup'){
            steps {
                echo '환경을 설정합니다'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Test') {
            steps {
                echo 'Unit 테스트를 실행합니다'
                sh '''
                . venv/bin/activate
                pytest test_calculator.py -v --junit-xml=unit-results.xml
                '''
            }
        }

        // stage('Intergration Test') {
        //     steps {
        //         echo 'Selenium 테스트를 실행합니다.'
        //         sh '''
        //         . venv/bin/activate
        //         pytest test_web.py -v --junit-xml=integration-results.xml
        //         '''
            // }
        // }

     post {
        always {
                echo '테스트 결과를 수집합니다.'
                junit '*-results.xml'
            }

        sucess {
                echo '모든 테스트 성공'
            }
        failure{
                echo '테스트 실패'
            }
        }
    }
}