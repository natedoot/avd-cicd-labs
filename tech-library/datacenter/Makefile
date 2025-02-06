.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: avd-deploy
avd-deploy: ## Deploy configurations to CV
	ansible-playbook playbooks/deploy.yml -i inventory.yml \
		-e cv_token=$(CV_SVC_TOKEN) \
		-e cv_workspace_name=$(CV_WS_NAME)

.PHONY: avd-build
avd-build: ## Build configurations using AVD
	ansible-playbook playbooks/build.yml -i inventory.yml

.PHONY: avd-deploy-rcc
avd-deploy-rcc: ## Deploy configurations using Change Control
	ansible-playbook playbooks/deploy.yml -i inventory.yml \
		-e cv_token=$(CV_SVC_TOKEN) \
		-e cv_run_change_control=True

.PHONY: avd-validate
avd-validate: ## Validate configurations using AVD
	ansible-playbook playbooks/validate.yml -i inventory.yml \
		-e ansible_user=$(ANSIBLE_USERNAME) \
		-e ansible_password=$(ANSIBLE_PASSWORD)

.PHONY: avd-server-build
avd-server-build:
	ansible-playbook playbooks/server-deploy-eapi.yml --tags build -i inventory.yml -e "target_hosts=SERVERS"

.PHONY: avd-server-deploy
avd-server-deploy:
	ansible-playbook playbooks/server-deploy-eapi.yml --tags deploy -i inventory.yml -e "target_hosts=SERVERS" 
