# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code + explanation

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Code block
  - **Output**: Rewritten code with consistent style

- **Complexity Analysis**
  - **Goal**: Identify and reduce Big O complexity or cyclomatic complexity
  - **Input**: Algorithm or function
  - **Output**: Analysis report and simplified alternative

## Debugging
- **Error Identification**
  - **Goal**: Find the root cause of a specific runtime or compile-time error
  - **Input**: Stack trace + relevant code snippet
  - **Output**: Explanation of the bug and a fix

- **Logical Flaw Detection**
  - **Goal**: Identify "silent" bugs where code runs but produces wrong output
  - **Input**: Code + expected vs. actual output
  - **Output**: Correction of the logical flow

- **Security Vulnerability Scanning**
  - **Goal**: Detect common security risks like SQL injection or XSS
  - **Input**: Source code
  - **Output**: List of vulnerabilities and patched code versions

## Documentation
- **Docstring Generation**
  - **Goal**: Automatically generate comprehensive documentation for functions/classes
  - **Input**: Raw source code
  - **Output**: Code with standardized docstrings (e.g., Javadoc, Google Style)

- **README Creation**
  - **Goal**: Summarize project functionality for high-level understanding
  - **Input**: Project structure and main scripts
  - **Output**: A professional README.md file

- **API Specification**
  - **Goal**: Convert code endpoints into structured API documentation
  - **Input**: Controller or Route files
  - **Output**: OpenAPI/Swagger specification text

## Testing
- **Unit Test Generation**
  - **Goal**: Increase code coverage with automated test cases
  - **Input**: Function or Class logic
  - **Output**: Test suite using framework (e.g., Jest, PyTest)

- **Edge Case Identification**
  - **Goal**: Find input values that might break the system
  - **Input**: Component requirements or code
  - **Output**: List of boundary conditions and corresponding test inputs

- **Mock Data Generation**
  - **Goal**: Create realistic datasets for integration testing
  - **Input**: Schema definition or JSON example
  - **Output**: Array of diverse, valid mock objects
