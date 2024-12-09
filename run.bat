@echo off

REM Build the Docker image
echo Building the Docker image...
docker build -t fixed-width-parser .
IF ERRORLEVEL 1 (
    echo Docker build failed. Exiting.
    exit /b 1
)

REM Run the Docker container
echo Running the Docker container...
docker run --rm -v %cd%:/app fixed-width-parser

REM Notify the user
echo Process completed! Check the output.csv file in the current directory.
pause
