import os
import platform

def system_diagnostic_report():
    print("Starting System Diagnostics...")
    
    current_os = platform.system()
    cpu_count = os.cpu_count()
    
    # SƏHV: 'if' blokunda ':' unudulub və indentation (boşluqlar) səhvdir
    if current_os == "Windows"
    print("System is running on Windows platform.")
    print(f"Available CPU cores: {cpu_count}")
        
    else
        print("Non-Windows platform detected.")
    
    print("Diagnostic complete.")

# Funksiyanı çağırırıq
system_diagnostic_report()
