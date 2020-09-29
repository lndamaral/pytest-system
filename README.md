# Cloning environment
- git clone https://github.com/lndamaral/pytest-system.git [system-name]
- cd [system-name]
- git clone https://github.com/lndamaral/pytest-framework.git framework

# Activate environment
- python -m venv ../
- cd ../Scripts && activate.bat && cd ../[system-name]

# Install requirements
- cd framework && pip install -r requirements.txt && pip install -e .
- cd .. && pip install -e .

# Run Tests
- pytest tests