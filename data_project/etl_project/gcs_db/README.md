## Procedure/Setup
Start Orion Server from CLI to check your Prefect UI:
`prefect orion start`

Make sure you find ***for_fetching_purposes*** folder for better understanding the process. Prefect will take the script from there and solve the API Managment for you. You do NOT need to download it.
I've also added the script in this folder, for completion purposes only. 

After adding *Github Block* from Prefect Orion UI, build a Docker image using `docker image build -t dieg0sc/prefect:hw .` 

Then push the image using `docker image push dieg0sc/prefect:hw`. This is crucial since the *Docker Block* will take the image from DockerHub.

I built the deployment using a python script. Execute it with `python docker_deploy.py`. Here I specified the storage (GitHub) and the infrastructure where it's going to be run (Docker).

Call the agent:
`prefect agent start -q default`

Finally, run the deployment from CLI:

`prefect deployment run etl-web-to-gcs/etl_github`

Before running the deployment, you can also schedule it from the UI or specify it from Command Line with something like this:

`prefect deployment build <script_name>:<flow_name> -n "deployment_name" --cron "0 5 1 * *" -a `

In this example, the CRON schedule is being used. This deployment will run the first of every month at 5AM UTC.


