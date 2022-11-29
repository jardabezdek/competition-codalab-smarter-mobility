## :rocket: competition-codalab-smarter-mobility

Repository with files created for Smarter mobility challenge, organised by
[Codalab](https://codalab.lisn.upsaclay.fr/).

## :pencil: Authors

- [Jaroslav Bezdek](https://www.github.com/jardabezdek)

## :construction_worker_man: Setup

### Local development

In order to create a working environment, the [docker](https://www.docker.com/)
is used. To start it, please, follow the next steps.

1. Launch the docker daemon.
1. Get to the repository root folder: `cd ~/projects/competition-codalab-smarter-mobility/`
1. Build the docker image with a proper tag: `docker build -t competition-codalab-smarter-mobility:latest .`
1. Run docker container: `docker run -it -p 8888:8888 -v $(pwd):/usr/src/app competition-codalab-smarter-mobility:latest /bin/bash`
1. Run notebook inside the docker container: `jupyter notebook --ip 0.0.0.0 --no-browser --allow-root`
