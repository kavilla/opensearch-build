void call(Map args = [:]) {
    String jobName = args.jobName ?: 'distribution-build-opensearch-dashboards'
    lib = library(identifier: 'jenkins@20211123', retriever: legacySCM(scm))
    def buildManifest = lib.jenkins.BuildManifest.new(readYaml(file: args.buildManifest))
    String artifactRootUrl = buildManifest.getArtifactRootUrl(jobName, args.buildId)
    echo "Artifact root URL: ${artifactRootUrl}"
    
    sh([
        './test.sh',
        'bwc-test',
        "${args.testManifest}",
        "--paths opensearch-dashboards=${artifactRootUrl}",
    ].join(' '))
}