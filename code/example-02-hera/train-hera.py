from hera.workflows import Steps, Workflow, Container
from hera.shared import global_config

# Configure Hera global settings
global_config.host = "https://localhost:2746"
global_config.token = ""  # Copy token value after "Bearer" from the `argo auth token` command
global_config.verify_ssl = False  # Set to False if you are using a self-signed certificate

# Define the container that runs the training job
train_container = Container(
    name="train",
    image="davidamat/image-reg:latest",
    command=["/entrypoint", "train"],
    resources={"limits": {"memory": "5Gi", "cpu": "2"}},
)

# Create the workflow
with Workflow(
    generate_name="training-hera-",
    entrypoint="training-steps",
    namespace="n1",
) as w:
    with Steps(name="training-steps"):
        train_container()

if __name__ == "__main__":
    w.create()
