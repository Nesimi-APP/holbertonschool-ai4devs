# Risk Assessment

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| Hardcoded credentials | High | Found in config.php |
| SQL Injection Vulnerability | High | User input is not properly sanitized in the login module |
| Missing unit tests | Medium | Critical modules untested, leading to potential regression issues |
| Deprecated API usage | High | Relies on removed PHP functions; will break in next update |
| Tight coupling | Medium | Objects are overly dependent on each other, making refactoring difficult |
| No logging | Low | Debugging system failures is harder due to lack of event traces |
| Exposure of Sensitive Error Messages | Medium | Stack traces are visible to users, revealing internal paths |
