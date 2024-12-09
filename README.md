# Fixed-Width File Parser

This project parses a fixed-width file into a CSV format based on the provided specifications. The solution is containerized with Docker for ease of use.

---

## **How to Use**

### **Prerequisites**
- Ensure **Docker** is installed and running on your system.
  - [Download Docker](https://www.docker.com/products/docker-desktop)

---

### **For All Users (Windows, macOS, Linux)**

#### **Step 1: Prepare the Environment**
1. Clone or download the repository to your local system.
2. Ensure the following files are in the project directory:
   - `fixed_width_to_csv.py`
   - `spec.json`
   - `input_fixed_width.txt`
   - `Dockerfile`
   - `run.bat` (for Windows)
   - `run.sh` (for macOS/Linux)


#### **Step 2: Run the Script**

1. **For Windows**:
   - Makesure to run the DockerDesktop app , until it shows on the taskbar as running
   - Double-click `run.bat` to build the Docker image and run the parser.


2. **For macOS/Linux**:
   - Open a terminal and navigate to the project directory:
   - Make the script executable (only required once):
     chmod +x run.sh
   - Run the script:
     ./run.sh

3. The `output.csv` file will be generated in the same directory as the scripts.

---


## **Optional: Docker Commands**
If you prefer running Docker commands manually instead of using the provided scripts:
1. **Build the Docker Image**:
   ```bash
   docker build -t fixed-width-parser .
