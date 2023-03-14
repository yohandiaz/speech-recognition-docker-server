node {
    stage('git checkout'){
        git branch: 'master', url: 'https://github.com/yohandiaz/speech-recognition-docker-server'
    }
    
    stage('Docker build image'){
        sh 'docker image build -t $JOB_NAME:v1.$BUILD_ID . '
        sh 'docker image tag $JOB_NAME:v1.$BUILD_ID yohandiaz/$JOB_NAME:v1.$BUILD_ID'
        sh 'docker image tag $JOB_NAME:v1.$BUILD_ID yohandiaz/$JOB_NAME:latest'
    }
    
    stage('Pushing images to Docker Hub and removing old images locally'){
        withCredentials([string(credentialsId: 'DockerHubPassword', variable: 'DockerPasswd')]) {
            sh "docker login -u yohandiaz -p ${DockerPasswd}"
            sh 'docker image push yohandiaz/$JOB_NAME:v1.$BUILD_ID'
            sh 'docker image push yohandiaz/$JOB_NAME:latest'
            
            sh 'docker image rm $JOB_NAME:v1.$BUILD_ID'
            sh 'docker image rm yohandiaz/$JOB_NAME:v1.$BUILD_ID'
            sh 'docker image rm yohandiaz/$JOB_NAME:latest'
        }
    }
    
    stage('Docker container deployment'){
        
        sshagent(['webapp_server']) {
            
            def docker_rmc = "docker container rm -f speech-recognition-webapp"
            def docker_rmi = "docker image rm -f yohandiaz/speech-recognition-webapp"
            def docker_run = "docker run -itd --name speech-recognition -p 81:81 yohandiaz/speech-recognition-webapp"
            
            sh "ssh -p 22 -o StrictHostKeyChecking=no vagrant@192.168.56.11 ${docker_rmc}"
            sh "ssh -p 22 -o StrictHostKeyChecking=no vagrant@192.168.56.11 ${docker_rmi}"
            sh "ssh -p 22 -o StrictHostKeyChecking=no vagrant@192.168.56.11 ${docker_run}"
        }
    }
}
