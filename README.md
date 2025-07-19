# Antisleep UI Automation Tests

This repository contains UI automation tests for the Antisleep web application, specifically focusing on the "Devices Report Export Flow" functionality. These tests are built using Python, Selenium, Pytest, and Allure for comprehensive reporting.
# URL for a required video demonstration: https://disk.yandex.ru/i/j74IaNIyoAju0g

## 🚀 Technologies Used

*   **Python**: Programming language
*   **Selenium WebDriver**: For browser automation
*   **Pytest**: Testing framework
*   **Allure Report**: For generating rich, interactive test reports

## ⚙️ Setup and Installation

To get this project up and running on your local machine, follow these steps:

### Prerequisites

*   **Python 3.x**: Make sure Python is installed on your system.
*   **Java Development Kit (JDK)**: Required for Allure Report to run. You can download it from [Oracle's website](https://www.oracle.com/java/technologies/javase-downloads.html) or use OpenJDK.
*   **Allure Commandline**: Install Allure Commandline globally. Instructions can be found on the [Allure GitHub page](https://github.com/allure-framework/allure-commandline#installation). For Windows, you can download the zip and add its `bin` directory to your system's PATH.

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <https://github.com/M501/UI-test>
    cd Anti_Sleep_A
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🧪 How to Run Test

Once the setup is complete, you can run the tests using Pytest.

1.  **Run the tests and generate Allure results:**
    ```bash
    python -m pytest --alluredir=allure-results
    ```
    This command will execute the tests and save the raw Allure results in the `allure-results` directory.

## 📊 Viewing Allure Report

After running the tests, you can generate and view the interactive Allure report.

1.  **Generate the Allure HTML report:**
    ```bash
    allure generate allure-results --clean -o allure-report
    ```
    This command processes the raw results and creates the HTML report in the `allure-report` directory. The `--clean` flag ensures a fresh report is generated each time.

2.  **Open the Allure report in your browser:**
    ```bash
    allure open allure-report
    ```
    This will launch your default web browser and display the generated Allure report, providing detailed insights into the test execution, including steps, timings, and statuses.
