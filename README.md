# Bluetooth Intrusion Detection System

## IoT Vulnerabilities: Case of Smart Watch

This project aims to develop a basic system for detecting and flagging Bluetooth intrusions in smartwatches using machine learning. The system includes data generation, model training, real-time detection, and a command-line interface for interaction.
After various experiments, an ROC Curve of 0.94 was achieved using Random Forest Model.

![Receiver Operations Characteristics](/output.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates a simple approach to detecting Bluetooth intrusions in wearable devices using machine learning. The main goal is to showcase the potential of AI/ML in enhancing the security of Bluetooth connections.

## Features

- Simulated dataset for Bluetooth connections.
- Logistic Regression and Random Forest model for intrusion detection.
- Real-time detection script.
- Command-line interface (CLI) for user interaction.
- Visualization of Bluetooth connections.

![Criteria for intrusion](/condition.png)

- [Criteria for Intrusion

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/joe-boadi/Bluetooth-intrusion-detection.git
    cd bluetooth-intrusion-detection
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

  ```bash
    pip install -r requirements.txt
```

- Example

```bash
pip install pandas numpy scikit-learn matplotlib
```
  
## Usage

1. **Generate the dataset:**

    ```bash
    python data_generation.py
    ```

2. **Train the model:**

    ```bash
    python model_training.py
    ```

3. **Run the command-line interface (CLI):**

    ```bash
    python cli_interface.py
    ```

The CLI provides options to display Bluetooth connections, simulate real-time detection, and exit the program.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the repository.**
2. **Create a new branch:**

    ```bash
    git checkout -b feature-name
    ```

3. **Make your changes and commit them:**

    ```bash
    git commit -m "Description of changes"
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature-name
    ```

5. **Submit a pull request.**

Please ensure your code follows the project's coding standards and passes all tests before submitting a pull request.

- [Intrusion detection systems for IoT-based smart ... - SpringerOpen.](https://journalofcloudcomputing.springeropen.com/articles/10.1186/s13677-018-0123-6)
- [A critical review of intrusion detection systems in the internet of ....](https://cybersecurity.springeropen.com/articles/10.1186/s42400-021-00077-7)
- [Intrusion Detection System (IDS): Types, Techniques, and Applications.](https://www.knowledgehut.com/blog/security/intrusion-detection-system)

## Some examples of intrusion detection system (IDS) applications

- [12 Best Intrusion Detection System (IDS) Software 2024 - Comparitech.](https://www.comparitech.com/net-admin/network-intrusion-detection-tools/)
- [Intrusion detection systems for IoT-based smart ... - SpringerOpen.](https://journalofcloudcomputing.springeropen.com/articles/10.1186/s13677-018-0123-6)
- [IoT-based smart environment using intelligent intrusion detection system.](https://link.springer.com/article/10.1007/s00500-021-06028-1)
- [Securing the Digital World: Protecting smart infrastructures and ....](https://arxiv.org/pdf/2401.01342)
- [A data-driven approach for intrusion and anomaly detection using ....]( https://link.springer.com/article/10.1007/s00500-023-09037-4)
- [An Embedded AI-Based Smart Intrusion Detection System for ... - Springer.](https://link.springer.com/chapter/10.1007/978-3-031-23201-5_2)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
