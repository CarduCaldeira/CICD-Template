# CICD-to-GPU-Projects

```
├── apiclient.py
├── assets
│   └── arch.png
├── Dockerfile
├── pyproject.toml
├── README.md
├── requirements_jarvis.txt
├── src
│   └── main.py
├── tests
│   └── pytorch_test.py
├── uv.lock
├── mkdocs.yml
├── docs
├── .githooks
│   └── pre-commit
└── .github
    └── workflows
        ├── development.yml
        ├── main.yml
        └── timeout.yml
```


- .github/workflows:

- src/main.py:

- requirements_jarvis.txt: Requierements used to install api client of Jarvis and resume and pause the instance in ci/cd workflow.

- Dockfile: 

- apiclient.py: Requierements used to install api client of Jarvis and resume and pause the instance in ci/cd workflow.

- tests/: Requierements used to install api client of Jarvis and resume and pause the instance in ci/cd workflow.

- .githooks:

## Ferramentas utilizadas


### UV

uv add torch==2.4.1 --index pytorch=https://download.pytorch.org/whl/cu121

### Git Hub Actions


### Jarvis

https://github.com/jarvislabsai/jlclient

### Docker

## Considerations

https://github.com/orgs/community/discussions/50926


