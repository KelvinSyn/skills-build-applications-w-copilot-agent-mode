# Python Version Update

This repository has been updated to use **Python 3.13** (the latest stable version) instead of the previous Python 3.12.3.

## What Changed

### Devcontainer Configuration
- Updated `.devcontainer/post_create.sh` to automatically install Python 3.13 when the devcontainer is built
- Python 3.13 is installed via the deadsnakes PPA for the latest stable release

### VS Code Configuration  
- Updated `.vscode/launch.json` to use Python 3.13 as the default Python interpreter
- Fixed Python path and environment configurations for debugging

### Testing
- Added Python version verification test to ensure Python 3.13 is properly installed
- Existing Django 4.1 requirements remain compatible

## Python 3.13 Benefits

- **Performance improvements**: Enhanced speed and efficiency
- **Better error messages**: More helpful debugging information  
- **Latest language features**: Access to newest Python capabilities
- **Security updates**: Latest security patches and improvements

## Compatibility

- **Django 4.1**: Continues to work with Python 3.13 (though Django 5.1+ is recommended for full support)
- **Dependencies**: All existing requirements in `requirements.txt` are compatible
- **Development workflow**: No changes needed to existing development processes

## Getting Started

1. Rebuild your devcontainer to get Python 3.13:
   ```bash
   # In VS Code: Ctrl/Cmd + Shift + P -> "Dev Containers: Rebuild Container"
   ```

2. Verify the Python version:
   ```bash
   python3 --version  # Should show Python 3.13.x
   ```

3. Run tests to verify everything works:
   ```bash
   cd octofit-tracker/backend
   python3 manage.py check
   ```

The upgrade is automatic and requires no manual intervention!