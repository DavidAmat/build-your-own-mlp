import os
import dotenv
from hera.shared import global_config
from hera.workflows import Steps, Workflow, script

dotenv.load_dotenv()

# print("Argo Host: ", os.getenv("ARGO_HOST", None))

# global_config.host = os.getenv("ARGO_SERVER", None)  # "https://<your-host-name>"
# global_config.token = os.getenv(
#     "ARGO_TOKEN", None
# )  # Copy token value after "Bearer" from the `argo auth token` command
# # global_config.image = "474902931812.dkr.ecr.eu-west-1.amazonaws.com/hi-python-mlp-base-image:latest"  # Set the image if you cannot access "python:3.8" via Docker Hub
# global_config.service_account_name = (
#     "hera-service-account"  # Set the service account name
# )
global_config.verify_ssl = False


@script()
def echo(message: str):
    print(message)


with Workflow(
    generate_name="hello-world-",
    entrypoint="steps",
    namespace=os.getenv("ARGO_NAMESPACE", "default"),
) as w:
    with Steps(name="steps"):
        echo(arguments={"message": "Hello world!"})

w.create()

wf = w.to_yaml()

print(wf)
