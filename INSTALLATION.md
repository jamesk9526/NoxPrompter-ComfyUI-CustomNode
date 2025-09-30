# Installation Guide for ComfyUI Nox Prompter

## Quick Installation

### Option 1: Git Clone (Recommended)
```bash
# Navigate to your ComfyUI custom_nodes directory
cd /path/to/ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/yourusername/ComfyNoxPrompter.git

# Restart ComfyUI
```

### Option 2: ComfyUI Manager
1. Open ComfyUI Manager
2. Search for "Nox Prompter"
3. Click Install
4. Restart ComfyUI

### Option 3: Manual Download
1. Download the ZIP file from the repository
2. Extract to `ComfyUI/custom_nodes/ComfyNoxPrompter/`
3. Restart ComfyUI

## Verification

After installation and restart:
1. Right-click in the ComfyUI workflow area
2. Look for "NoxPrompter" in the node categories
3. You should see three nodes:
   - Nox Prompt Enhancer
   - Nox Prompt Combiner  
   - Nox Prompt Analyzer

## Troubleshooting

### Nodes don't appear
- Make sure the folder is named exactly `ComfyNoxPrompter`
- Verify all files are present: `__init__.py`, `NoxPromptNode.py`
- Check ComfyUI console for error messages
- Restart ComfyUI completely

### Import errors
- Ensure you're using Python 3.7 or higher
- No additional dependencies are required

### Need help?
- Check the README.md for detailed usage instructions
- Run `python test_nodes.py` to verify installation
- Create an issue on GitHub if problems persist

## File Structure Check
Your installation should look like this:
```
ComfyUI/
└── custom_nodes/
    └── ComfyNoxPrompter/
        ├── __init__.py
        ├── NoxPromptNode.py
        ├── README.md
        ├── LICENSE
        ├── test_nodes.py
        ├── INSTALLATION.md
        └── examples/
            └── README.md
```