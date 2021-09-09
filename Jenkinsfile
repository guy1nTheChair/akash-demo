pipeline{
    stages{
        stage("build"){
            sh "docker build -t guyinthechair/akash-demo:latest ."
        }
        stage("push"){
            sh "docker push guyinthechair/akash-demo:latest"
        }
    }
}