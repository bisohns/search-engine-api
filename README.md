# search-engine-api

A public API for the [search-engine-parser](https://github.com/bisoncorps/search-engine-parser) library 
<hr>

[![Build Status](https://travis-ci.com/bisoncorps/search-engine-api.svg?branch=master)](https://travis-ci.com/bisoncorps/search-engine-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<hr/>

To extend the application of search-engine-parser to other languages for querying all types of popular search engines on [search-engine-parser](https://github.com/bisoncorps/search-engine-parser). The API was built using [Fast API](https://github.com/tiangolo/fastapi).

- Search Engine API
  - [Installation](#installation)
  - [Running the tests](#running-the-tests)
  - [Usage](#usage)

## Popular Supported Engines

Some of the popular search engines include:

- Google
- DuckDuckGo
- GitHub
- StackOverflow
- Baidu
- YouTube

View all [supported engines](https://github.com/bisoncorps/search-engine-parser/blob/master/docs/supported_engines.md)

## Installation

### Poetry
```bash
    # install only package dependencies
    poetry install
    # Installs `pysearch` cli  tool
    uvicorn main:app --reload
```

## Running the tests

```bash
    pytest
```

## Usage
When the server is started, the Swagger UI is available at http://localhost:8000/swagger for testing


![Demo](assets/swagger-ui.png)
