Exercise 3: Environment Variable Usage Image

Description: This image will echo an environment variable when run.

Before Starting your Dockerfile:

1. Create a directory named `exercise3-env-var`.

Instructions:

1. Use the alpine image as your base.
2. Create a new directory named `env`.
3. Set this as your work directory.
4. Use the ENV command to set an environment variable
   1. var name : myVar
   2. var value : "Hello, Docker!"
5. Print the working directory and environment variable when the container starts - use the following command -`sh -c "echo Current directory: $(pwd) && echo $myVar"`
   \*\* Note: The `sh -c` command is used to run multiple commands in a single RUN instruction.

Docker commands:

```bash
docker build -t my-env-image .

docker run -it my-env-image
```
