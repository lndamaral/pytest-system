# Activate environment
- python -m venv ../
- ../Scripts/activate.bat

# Cloning environment
- git clone https://github.com/lndamaral/pytest-system.git [system-name]
- cd [system-name]
- git clone https://github.com/lndamaral/pytest-framework.git framework

# Install requirements
- cd framework
- pip install -r requirements.txt
- cd ..
- pip install -e .