# ELIXIR Crate DB

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Development Status](https://img.shields.io/badge/status-beta-yellow.svg)](https://github.com/elixir-cloud-aai/TESK)
[![GitHub contributors](https://img.shields.io/github/contributors/elixir-cloud-aai/crate-db)](https://github.com/elixir-cloud-aai/crate-db/graphs/contributors)
[![Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://docs.astral.sh/ruff/)

## Introduction

Various research artifacts are produced daily around the world, but managing them is a tedious task for researchers. Researchers prefer to spend more time on new discoveries rather than finding efficient ways to store, retrieve, or share their data. This project aims to alleviate these challenges by providing a robust backend system for managing RO-Crates—standardized packages for research data and metadata.

## User Story

The end user (research publisher/scientist) will be able to manage any of the RO-Crates developed for personal or public research. The main functions include CRUD operations on RO-Crates and publishing them to Zenodo. This project can be summarized as an "Efficient RO-Crate Management System". Future enhancements include developing a frontend component to further simplify these operations.

## Project Goals & Milestones

### Goals
- Develop a scalable and extendible Flask app using FOCA.
- Implement efficient search functionality using ElasticSearch.
- Enable access controls over the application.
- Create endpoints for publishing/unpublishing RO-Crates to/from Zenodo.
- Package the project as a Python dependency.
- Write examples, tests, and documentation.

## Implementation Details

### Abstract
The project focuses on developing a backend system for managing RO-Crates via API endpoints. The system provides functionalities for storing, retrieving, publishing, and unpublishing RO-Crates.

### Flow
- **Storage:** Researchers submit RO-Crate data and metadata via API endpoints. The system validates and stores the data securely.
- **Retrieval:** Researchers query the system via API endpoints to locate specific RO-Crates. The system returns the data in the specified format.
- **Publishing/Unpublishing:** Integration with Zenodo allows researchers to publish/unpublish RO-Crates. API endpoints facilitate these processes.

### Architecture
Three main components will be used:
1. **MinIO:** Serves as an object storage system for storing zipped RO-Crates.
2. **MongoDB:** Stores metadata and zipped RO-Crates.
3. **RO-Crate Microservice:** Central package interacting with other components.

### Why MinIO?
MinIO is chosen for its high performance, scalability, cloud-native compatibility, security features, and cost-effectiveness. It supports object storage, horizontal scaling, and built-in encryption, making it ideal for our project's needs.

## Technical Details

### Technologies
- **FOCA:** Enables fast development of OpenAPI-based HTTP API microservices in Flask.
- **MongoDB and MinIO:** Used for storage.
- **Zenodo APIs:** Used for publishing research artifacts.

### Challenges
1. **Complexity of RO-Crate Structure:** Designing efficient storage and retrieval mechanisms.
2. **Integration with External Services:** Handling authentication, authorization, and error handling.
3. **Optimizing Performance:** Ensuring efficient uploads, downloads, and search operations.
4. **Security and Data Integrity:** Protecting sensitive data and ensuring integrity during transmission and storage.

## Future Prospects

Future development will focus on thorough implementation of CRUD operations, emphasizing simplicity and robustness. Stretch goals include advanced operations and developing a frontend component for enhanced user interaction and accessibility. This project aims to evolve into a comprehensive solution for managing RO-Crates efficiently and effectively.
