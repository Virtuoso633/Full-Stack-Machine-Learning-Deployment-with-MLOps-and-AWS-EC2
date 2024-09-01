# Full-Stack Machine Learning Deployment with MLOps and AWS EC2


## Workflows


---

# End-to-End Machine Learning Project with MLflow

This project demonstrates an end-to-end machine learning pipeline using MLflow for model tracking and management. Below is the detailed workflow and purpose for each step in the project.

## Workflows

### 1. Update `config.yaml`

**Purpose**:  
The `config.yaml` file typically contains configuration settings for your application or project, such as paths, environment variables, or other configurable parameters.

**Action**:  
Modify the `config.yaml` file to adjust settings related to your project. Ensure all required paths, environment variables, and other configuration parameters are updated.

---

### 2. Update `schema.yaml`

**Purpose**:  
The `schema.yaml` file defines the structure of your data, including columns and their data types.

**Action**:  
Ensure that `schema.yaml` accurately reflects the structure of your data. Update the schema as needed to match any changes in your data structure (e.g., adding/removing columns or changing types).

---

### 3. Update `params.yaml`

**Purpose**:  
This file contains parameters for various components of your project. It allows users to modify parameters without directly changing the code.

**Action**:  
Update the `params.yaml` file to include all necessary parameters for your project. Ensure that the file reflects any newly introduced or modified parameters.

---

### 4. Update the Entities

**Purpose**:  
Entities represent the core data structures or objects in your project.

**Action**:  
Modify or add entities as required to reflect changes in your data or project requirements. Ensure that the entities stay in sync with the data and model expectations.

---

### 5. Update the Configuration Manager in `src/config`

**Purpose**:  
The configuration manager is responsible for loading and managing configuration files such as `config.yaml`, `schema.yaml`, and `params.yaml`.

**Action**:  
Update the configuration manager to ensure it properly loads and applies the latest changes from the updated configuration files. This may include adding new configuration parameters or handling new data schema fields.

---

### 6. Update the Components

**Purpose**:  
Components represent the individual modules or functions in your project, such as data ingestion, validation, or processing.

**Action**:  
Make necessary updates to the components to accommodate changes in configuration, schema, or parameters. Ensure that components are functioning properly and are aligned with the overall pipeline.

---

### 7. Update the Pipeline

**Purpose**:  
The pipeline integrates all components and manages the workflow for tasks such as data ingestion, training, and prediction.

**Action**:  
Ensure that the pipeline is updated to reflect changes in components and configuration. This includes revising any steps in the training and prediction processes that need adjustment.

---

### 8. Update `main.py`

**Purpose**:  
`main.py` typically serves as the entry point for your application. It ties together the pipeline and components, handling tasks such as starting model training or making predictions.

**Action**:  
Update `main.py` to reflect any changes in the pipeline, components, or new functionality. Ensure that all components are called in the correct sequence and that the application runs smoothly from start to finish.

---

## Additional Information

- **MLflow Integration**: This project uses MLflow for tracking experiments, managing model versions, and serving models. Ensure that MLflow is configured correctly and linked to your ML pipeline.
  
- **Testing and Validation**: Regularly test your pipeline after updates to ensure that all components are working as expected and that the changes do not introduce any errors.

- **Deployment**: Depending on your project goals, you may want to deploy your model to a cloud platform or serve it via an API. Consider using AWS EC2 or similar services for deployment.

---

