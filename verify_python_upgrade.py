#!/usr/bin/env python3
"""
Verification script for Python 3.13 upgrade
Run this after devcontainer rebuild to verify the upgrade was successful
"""

import sys
import subprocess

def main():
    print("🔍 Verifying Python 3.13 Upgrade...")
    print("="*50)
    
    # Check Python version
    version = sys.version_info
    print(f"📦 Python Version: {version.major}.{version.minor}.{version.micro}")
    
    # Check if we have Python 3.13+
    if version.major == 3 and version.minor >= 13:
        print("✅ SUCCESS: Python 3.13+ is installed!")
        success = True
    else:
        print("⚠️  WARNING: Python version is not 3.13+")
        print("   The devcontainer may need to be rebuilt.")
        success = False
    
    # Check Python executable path
    print(f"📍 Python Executable: {sys.executable}")
    
    # Check if we can import Django
    try:
        import django
        print(f"✅ Django {'.'.join(map(str, django.VERSION[:3]))} is available")
        django_ok = True
    except ImportError:
        print("❌ Django is not available - run 'pip install -r requirements.txt'")
        django_ok = False
    
    # Summary
    print("\n" + "="*50)
    if success and django_ok:
        print("🎉 All checks passed! Python 3.13 upgrade successful!")
        print("\n💡 You can now use the latest Python features in your Django application.")
    elif success:
        print("✅ Python 3.13 is installed successfully!")
        print("📝 Install Django requirements: pip install -r octofit-tracker/backend/requirements.txt")
    else:
        print("🔧 Action needed: Please rebuild the devcontainer to get Python 3.13")
        print("   In VS Code: Ctrl/Cmd + Shift + P -> 'Dev Containers: Rebuild Container'")
    
    return success and django_ok

if __name__ == "__main__":
    main()