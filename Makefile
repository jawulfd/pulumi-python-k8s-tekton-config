.PHONY: pulumi-init
stack-up:
    @echo "Initializing tekton stack"
    @pulumi stack init tekton

.PHONY: pulumi-preview-plan
stack-up:
    @echo "Generating plan file"
    @pulumi preview --save-plan=plan.json

.PHONY: pulumi-apply-plan
stack-up:
    @echo "Applying plan file"
    @pulumi up --plan=plan.json