#REMEMBER TO COPY TO /week_2/ after finishing

from prefect.deployments import Deployment
from prefect.infrastructure.docker import DockerContainer
from github_web_to_gcs import etl_web_to_gcs
from prefect.filesystems import GitHub

github_block = GitHub.load("zoom-hw")

docker_block = DockerContainer.load("zoom")

docker_dep = Deployment.build_from_flow( 
    flow=etl_web_to_gcs,
    name='etl_github',
    infrastructure=docker_block,
    storage=github_block
)

if __name__ == "__main__":
    docker_dep.apply()


