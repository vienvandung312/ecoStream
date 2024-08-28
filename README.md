# ecoStream
A real-time data streaming platform to monitor environmental conditions across different locations. \
The platform will ingest data from IoT devices such as weather stations and air quality sensors, process the data in real-time, store it in a scalable data warehouse, and visualize it through an interactive dashboard.

## Data Sources 

### 1. Weather Data:
- __Source:__ Simulated IoT devices or APIs (e.g., OpenWeatherMap API).
- __Data Points:__ Temperature, humidity, wind speed, precipitation.

### 2. Air Quality Data:
- __Source:__ Simulated air quality sensors or APIs (e.g., AirVisual API).
- __Data Points:__ PM2.5, PM10, CO2 levels, NO2 levels.

### 3. Geolocation Data:
- __Source:__ GPS devices or APIs (e.g., Google Maps API).
- __Data Points:__ Latitude, longitude, altitude.

### 4. Additional Environmental Data:
- __Source:__ Simulated sensors or APIs (e.g., Soil Moisture API).
- __Data Points:__ Soil moisture levels, UV index.

## Features

- Real-time data streaming from IoT devices
- Data processing in real-time
- Scalable data warehousing
- Interactive dashboard for data visualization

## Tech Stack:

### 1. Data Ingestion:

#### Apache Kafka:
- Use: Stream data from simulated IoT devices in real-time.
- Setup: Kafka topics will be set up for each data source (e.g., weather, air quality, geolocation).

### 2. Data Processing:

#### Apache Spark Streaming:
- Use: Real-time processing of the ingested data streams.
- Functionality: Perform transformations, aggregations, and filtering on the data (e.g., calculating rolling averages for temperature, identifying spikes in pollution levels).

### 3. Data Storage:

#### AWS S3:
- Use: Store raw, unprocessed data for quick retrieval and backup.

#### Amazon Redshift:
- Use: Store processed and aggregated data for long-term analytics.
- Functionality: Enable complex queries and historical data analysis.

### 4. Real-Time Analytics and Visualization:

#### Grafana:
- Use: Create real-time dashboards to monitor environmental metrics.
- Functionality: Set up dashboards with various visualizations (e.g., heatmaps, line charts, geographic maps).

#### Elasticsearch + Kibana (Optional):
- Use: Index and visualize logs or time-series data, useful for more detailed analytics and anomaly detection.

### 5. Alerting and Notifications:

#### Prometheus + Alertmanager:
- Use: Monitor specific metrics and trigger alerts (e.g., when air quality deteriorates beyond a certain threshold).

#### Slack API or Twilio:
- Use: Send real-time alerts via Slack or SMS.

### 6. Security and Data Governance:

#### AWS IAM:
- Use: Manage access control for your cloud-based resources.

#### AWS KMS:
- Use: Encrypt sensitive data at rest and in transit.

### 7. Deployment and Infrastructure:

#### Terraform:
- Use: Define and provision the cloud infrastructure (e.g., EC2 instances, S3 buckets).

#### Docker:
- Use: Containerize your applications for easy deployment and scaling.

#### AWS Lambda (Optional):
- Use: Trigger serverless functions for lightweight processing tasks or automated alerts.

### 8. CI/CD Pipeline:

#### Jenkins or GitLab CI:
- Use: Automate the building, testing, and deployment of your platform.

#### Ansible:
- Use: Automate configuration management and application deployment.


## Contact

If you have any questions or suggestions, feel free to reach out to us at [this mail](vienvandung312@gmail.com).
