# ELIXIR Crate DB

[![License][badge-license]][badge-url-license]
[![Python 3.11][badge-python]][badge-url-python]
[![Development Status][badge-status]][badge-url-status]
[![GitHub contributors][badge-contributors]][badge-url-contributors]
[![Ruff][badge-ruff]][badge-url-ruff]

## Introduction

Various research artifacts are produced daily around the world, but 
managing them is a tedious task for researchers. Researchers prefer to 
spend more time on new discoveries rather than finding efficient ways to 
store, retrieve, or share their data. This project aims to alleviate 
these challenges by providing a robust backend system for managing 
RO-Crates—standardized packages for research data and metadata.

## User Story

The end user (research publisher/scientist) will be able to manage any 
of the RO-Crates developed for personal or public research. The main 
functions include CRUD operations on RO-Crates and publishing them to 
Zenodo. This project can be summarized as an "Efficient RO-Crate 
Management System". Future enhancements include developing a frontend 
component to further simplify these operations.

## Project Goals & Milestones

### Goals

- Develop a scalable and extensible [Flask][flask] app using [FOCA][foca].
- Implement efficient search functionality using 
  [ElasticSearch][elasticsearch].
- Enable access controls over the application.
- Create endpoints for publishing/unpublishing RO-Crates to/from 
  [Zenodo][zenodo].
- Package the project as a Python dependency.
- Write examples, tests, and documentation.

## Implementation Details

### Abstract

The project focuses on developing a backend system for managing 
RO-Crates via API endpoints. The system provides functionalities for 
storing, retrieving, publishing, and unpublishing RO-Crates.

### Flow

- **Storage:** Researchers submit RO-Crate data and metadata via API 
  endpoints. The system validates and stores the data securely.
- **Retrieval:** Researchers query the system via API endpoints to 
  locate specific RO-Crates. The system returns the data in the 
  specified format.
- **Publishing/Unpublishing:** Integration with [Zenodo][zenodo] allows 
  researchers to publish/unpublish RO-Crates. API endpoints facilitate 
  these processes.

### Architecture

Three main components will be used:

1. **[MinIO][minio]:** Serves as an object storage system for storing 
   zipped RO-Crates.
2. **[MongoDB][mongodb]:** Stores metadata and zipped RO-Crates.
3. **RO-Crate Microservice:** Central package interacting with other 
   components.

### Why MinIO?

MinIO is chosen for its high performance, scalability, cloud-native 
compatibility, security features, and cost-effectiveness. It supports 
object storage, horizontal scaling, and built-in encryption, making it 
ideal for our project's needs.

## Technical Details

### Technologies

- **[FOCA][foca]:** Enables fast development of OpenAPI-based HTTP API 
  microservices in [Flask][flask].
- **[MongoDB][mongodb] and [MinIO][minio]:** Used for storage.
- **[Zenodo APIs][zenodo]:** Used for publishing research artifacts.

### Challenges

1. **Complexity of RO-Crate Structure:** Designing efficient storage 
   and retrieval mechanisms.
2. **Integration with External Services:** Handling authentication, 
   authorization, and error handling.
3. **Optimizing Performance:** Ensuring efficient uploads, downloads, 
   and search operations.
4. **Security and Data Integrity:** Protecting sensitive data and 
   ensuring integrity during transmission and storage.

## Future Prospects

Future development will focus on thorough implementation of CRUD 
operations, emphasizing simplicity and robustness. Stretch goals 
include advanced operations and developing a frontend component for 
enhanced user interaction and accessibility. This project aims to 
evolve into a comprehensive solution for managing RO-Crates efficiently 
and effectively.

## Contributing

This project is a community effort and lives off your contributions, be 
it in the form of bug reports, feature requests, discussions, ideas, 
fixes, or other code changes. Please read [these guidelines][docs-contributing] 
if you want to contribute. And please mind the [code of conduct][docs-coc] 
for all interactions with the community.

## Versioning

The project adopts the [semantic versioning][semver] scheme for 
versioning. Currently, the service is in alpha stage, so the API may 
change and even break without further notice.

## License

This project is covered by the [Apache License 2.0][badge-url-license] 
also [shipped with this repository][docs-license].

## Contact

Crate-DB is part of [ELIXIR Cloud & AAI][res-elixir-cloud-aai], a 
multinational effort at establishing and implementing FAIR data sharing 
and promoting reproducible data analyses and responsible data handling 
in the life sciences.

If you have suggestions for or find issue with this app, please use the 
[issue tracker][contact-issue-tracker]. If you would like to reach out 
to us for anything else, you can join our [Slack board][badge-url-chat], 
start a thread in our [Q&A forum][contact-qa], or send us an 
[email][contact-email].

[![GA4GH logo](images/logo-ga4gh.png)](https://www.ga4gh.org/)  
[![ELIXIR logo](images/logo-elixir.png)](https://www.elixir-europe.org/)  
[![ELIXIR Cloud & AAI logo](images/logo-elixir-cloud.png)](https://elixir-europe.github.io/cloud/)

[badge-license]: <https://img.shields.io/badge/License-Apache_2.0-blue.svg>
[badge-python]: <https://img.shields.io/badge/python-3.11-blue.svg>
[badge-status]: <https://img.shields.io/badge/status-alpha-yellow.svg>
[badge-contributors]: <https://img.shields.io/github/contributors/elixir-cloud-aai/crate-db>
[badge-ruff]: <https://img.shields.io/badge/code%20style-ruff-000000.svg>
[badge-url-license]: ./LICENSE
[badge-url-python]: <https://www.python.org/downloads/release/python-311/>
[badge-url-status]: <https://github.com/elixir-cloud-aai/crate-db>
[badge-url-contributors]: <https://github.com/elixir-cloud-aai/crate-db/graphs/contributors>
[badge-url-ruff]: <https://docs.astral.sh/ruff/>
[contact-email]: <mailto:cloud-service@elixir-europe.org>
[contact-issue-tracker]: <https://github.com/elixir-cloud-aai/landing-page/issues>
[contact-qa]: <https://github.com/elixir-cloud-aai/elixir-cloud-aai/discussions>
[docs-coc]: <https://github.com/elixir-cloud-aai/elixir-cloud-aai/blob/dev/CODE_OF_CONDUCT.md>
[docs-contributing]: <https://elixir-cloud-aai.github.io/guides/guide-contributor/>
[docs-license]: LICENSE
[elasticsearch]: <https://www.elastic.co/elasticsearch/>
[zenodo]: <https://zenodo.org/>
[flask]: <https://flask.palletsprojects.com/en/3.0.x/>
[foca]: <https://github.com/elixir-cloud-aai/foca>
[minio]: <https://min.io/>
[mongodb]: <https://www.mongodb.com/>
[res-elixir-cloud-aai]: <https://elixir-cloud.dcc.sib.swiss/>
[semver]: <https://semver.org/>
