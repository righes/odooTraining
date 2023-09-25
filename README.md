# tuto for developper 
https://www.odoo.com/documentation/16.0/developer/tutorials/getting_started/02_setup.html 
# Odoo Technical Training Sandbox

![Odoo Logo](https://upload.wikimedia.org/wikipedia/commons/5/50/Odoo_logo.svg)

Welcome to the **Odoo Technical Training Sandbox** repository. This repository serves as a sandbox environment for learning and practicing Odoo development concepts. Whether you're a beginner looking to dive into Odoo development or an experienced developer aiming to sharpen your skills, this sandbox provides a hands-on space to experiment with various Odoo features and modules.

## Table of Contents

- [About Odoo](#about-odoo)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Features](#features)

## About Odoo

[Odoo](https://www.odoo.com/) is an open-source suite of business applications, including customer relationship management (CRM), e-commerce, inventory management, accounting, and more. It provides a platform for companies of all sizes to manage various business processes in an integrated manner.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites:

- [Docker](https://www.docker.com/get-started)

### Setting Up the Development Environment

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/omermecitoglu/odoo-technical-training-sandbox.git
   ```

2. Navigate to the project directory:

   ```bash
   cd odoo-technical-training-sandbox
   ```

3. Open the `docker-compose.yml` file and ensure that the following settings match your requirements:

   - `POSTGRES_USER`: The PostgreSQL user for the Odoo database.
   - `POSTGRES_PASSWORD`: The password for the PostgreSQL user.
   - `OE_VERSION`: The desired Odoo version (e.g., 13.0).

4. Start the Odoo development environment using Docker Compose:

   ```bash
   docker-compose up -d
   ```

5. Access the Odoo web interface by opening your browser and navigating to `http://localhost:8069`.

## Features

This sandbox repository includes the following features:

- Sample Odoo modules to demonstrate various development concepts.
- An organized structure to help you understand and experiment with different aspects of Odoo development.
- Code examples, comments, and documentation to guide you through the learning process.

Feel free to explore the existing modules and create your own to practice and test your Odoo development skills.
