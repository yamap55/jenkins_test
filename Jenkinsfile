try {
    node {
        stage("git_checkout") {
            checkout scm
        }
        stage("first") {
            println "最初のステージ？"
        }
        stage("second") {
            println "ステージ2？"
            sh 'python --version'
        }
        stage("third") {
            println "ステージ3？"
        }
	stage("four") {
	    sh "python ./test.py"
	}
    }
} catch(e) {
    println "エラー処理"
    e.printStackTrace()
    println "エラー処理終わり"
}
println "テスト1です。"
