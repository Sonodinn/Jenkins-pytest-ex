// Jenkinsfile (Declarative Pipeline)
pipeline {
    // 빌드 단계를 실행할 에이전트 환경을 정의합니다.
    agent {
        // python:3.11-slim 이미지를 사용하여 
        // Python과 필요한 도구가 이미 설치된 격리된 환경을 생성합니다.
        docker {
            image 'python:3.11-slim' 
            args '-u root' // 파일 권한 문제 방지를 위해 root로 실행
        }
    }

    // 환경 변수 설정 (필요한 경우)
    environment {
        // 테스트 결과 파일 경로를 변수로 지정
        TEST_RESULTS = 'test-results.xml' 
    }

    // 파이프라인의 핵심 단계들
    stages {
        stage('Prepare Environment') {
            steps {
                // venv 생성 및 활성화
                sh 'python3 -m venv venv'
                
                // 가상 환경 내의 pip을 사용하여 pytest와 selenium 설치
                sh 'venv/bin/pip install pytest selenium'
                
                // (선택) requirements.txt 파일이 있다면 이 명령어로 대체 가능:
                // sh 'venv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Starting pytest execution...'
                // 가상 환경 내의 pytest 실행. 
                // --junit-xml 옵션으로 보고서 파일을 생성합니다.
                sh "venv/bin/pytest test_calculator.py -v --junit-xml=${TEST_RESULTS}"
            }
        }
    }

    // 파이프라인 실행 후 항상 실행되는 단계 (정리 및 보고서 발행)
    post {
        always {
            echo 'Publishing test results...'
            // JUnit 플러그인을 사용하여 테스트 결과 보고서를 젠킨스에 등록합니다.
            junit "${TEST_RESULTS}" 
            
            // 작업 완료 후 가상 환경 삭제 (선택 사항)
            sh 'rm -rf venv'
        }
        failure {
            echo 'Build failed! Check logs for details.'
        }
    }
}