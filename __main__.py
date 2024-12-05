import pulumi
import pulumi_kubernetes as kubernetes

config = pulumi.Config()

tekton_pipelines_version = config.get("tektonPipelinesVersion", "v0.65.3")
tekton_triggers_version = config.get("tektonTriggersVersion", "v0.29.1")
tekton_dashboard_version = config.get("tektonDashboardVersion", "v0.52.0")


tekton_pipelines_release = kubernetes.yaml.v2.ConfigFile(
    "tekton-pipelines",
    file=f"https://storage.googleapis.com/tekton-releases/pipeline/previous/{tekton_pipelines_version}/release.yaml"
)

tekton_triggers_release = kubernetes.yaml.v2.ConfigFile(
    "tekton-triggers",
    file=f"https://storage.googleapis.com/tekton-releases/triggers/previous/{tekton_triggers_version}/release.yaml",
    opts=pulumi.ResourceOptions(depends_on=tekton_pipelines_release)
)

tekton_interceptors_release = kubernetes.yaml.v2.ConfigFile(
    "tekton-interceptors",
    file=f"https://storage.googleapis.com/tekton-releases/triggers/previous/{tekton_triggers_version}/interceptors.yaml",
    opts=pulumi.ResourceOptions(depends_on=tekton_triggers_release)
)

tekton_dashboard_release = kubernetes.yaml.v2.ConfigFile(
    "tekton-dashboard",
    file=f"https://storage.googleapis.com/tekton-releases/dashboard/previous/{tekton_dashboard_version}/release.yaml",
    opts=pulumi.ResourceOptions(depends_on=tekton_interceptors_release)
)

tekton_ingress = kubernetes.yaml.v2.ConfigFile(
    "tekton_ingress",
    file="resources/tekton/tektonci-ingress.yaml",
    opts=pulumi.ResourceOptions(depends_on=tekton_dashboard_release)
)
