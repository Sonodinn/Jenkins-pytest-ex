# 1. 젠킨스 공식 이미지를 기반으로 시작합니다. (lts-jdk17 버전을 추천)
FROM jenkins/jenkins:lts-jdk17

# 2. root 권한으로 전환하여 패키지를 설치합니다.
USER root

# 3. apt-get(우분투/데비안 계열 패키지 매니저)로 python3와 venv를 설치합니다.
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# 4. 다시 jenkins 유저로 복귀합니다. (보안)
USER jenkins