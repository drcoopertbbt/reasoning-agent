# O-RAN Agent Workflow APIs

This project contains two services for managing and analyzing O-RAN agent workflows. One service provides JSON data through an Express API, while the other service integrates with OpenAI's GPT-4 for generating responses based on network data using FastAPI.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Express API](#express-api)
  - [Routes](#routes)
  - [Test with cURL](#test-with-curl)
- [FastAPI Service](#fastapi-service)
  - [Endpoints](#endpoints)
  - [Running the Frontend](#running-the-frontend)
- [Usage](#usage)

## Requirements

- Node.js (v14+)
- Python 3.8+
- OpenAI API Key (for GPT-4 integration)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/oran-agent-workflows.git
    cd oran-agent-workflows
    ```

2. **Install dependencies for the Express API**:
    ```bash
    cd express-service
    npm install
    ```

3. **Install dependencies for the FastAPI service**:
    ```bash
    cd ../fastapi-service
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

   - Create a `.env` file inside the `fastapi-service` folder:
     ```bash
     OPENAI_API_KEY=your_openai_api_key
     ```

## Express API

The Express API serves JSON data to various endpoints related to centralized alarms, fault detection, root cause analysis, and more.

### Routes

The following routes are exposed by the Express API:

| Route                                     | Description                                              |
|-------------------------------------------|----------------------------------------------------------|
| `/api/centralized-alarm`                  | Returns data for centralized alarm collection            |
| `/api/root-cause-analysis`                | Returns data for root cause analysis                     |
| `/api/automated-fault-detection`          | Returns data for automated fault detection               |
| `/api/yang-models-fault-reporting`        | Returns data for YANG models fault reporting             |
| `/api/alarm-logging-data-analysis`        | Returns data for alarm logging and historical analysis    |
| `/api/real-time-visualization`            | Returns data for real-time visualization                 |
| `/api/collaborate-across-teams`           | Returns data on team collaboration for alarm management  |
| `/api/alarm-design-best-practices`        | Returns alarm design best practices data                 |

### Test with cURL

You can test the API routes using the following `curl` commands:

```bash
# Centralized Alarm Collection
curl http://localhost:3005/api/centralized-alarm

# Root Cause Analysis
curl http://localhost:3005/api/root-cause-analysis

# Automated Fault Detection
curl http://localhost:3005/api/automated-fault-detection

# YANG Models Fault Reporting
curl http://localhost:3005/api/yang-models-fault-reporting

# Alarm Logging and Historical Data Analysis
curl http://localhost:3005/api/alarm-logging-data-analysis

# Real-Time Visualization
curl http://localhost:3005/api/real-time-visualization

# Collaborate Across Teams
curl http://localhost:3005/api/collaborate-across-teams

# Alarm Design Best Practices
curl http://localhost:3005/api/alarm-design-best-practices
