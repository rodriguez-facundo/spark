# Build Spark image

## Steps

```bash
cd 2.4.4/libexec
./bin/docker-image-tool.sh -r <registry/username> -t <tag> build
```

NOTES:

- The script will build 3 images: spark, spark-py and spark-r.

- `-r` is not the name of the images but the name of the registry plus user name. For example, `r.cfcr.io/metacell` or `docker.io/mnp`. It can be omited.

- `-t` is the tag of the image. For instance, `v0.01` will give `spark:v0.01`, `spark-py:v0.01` and `spark-r:v0.01`.

- The script need to run on the folder `libexec`.
