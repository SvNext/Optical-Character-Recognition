service_name = cliq-image-to-table-service
repository = europe-west3-docker.pkg.dev/dynamic-shift-380619/docker-repo/${service_name}
region = europe-west3
port = 8000


build:
	docker build -t ${service_name} .
	docker tag ${service_name} $(repository)

run:
	docker run --rm --net=host --env-file=./.env ${service_name}

push:
	docker push $(repository)


deploy:
	gcloud run deploy ${service_name} \
		--image ${repository} \
		--cpu=2 \
		--max-instances=1 \
		--memory=2Gi \
		--min-instances=1 \
		--allow-unauthenticated \
		--port=${port} \
		--region=${region}

delete:
	gcloud run services delete ${service_name} --region=${region}

describe:
	gcloud run services describe ${service_name} --region=${region}

list:
	gcloud run services list