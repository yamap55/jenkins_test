try {
    node {
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
    }
} catch(e) {
    println "エラー処理"
}
println "テスト1です。"
