# Learning-Log
## Requirements
- Anaconda 23.7.4
- Python 3.11.5
- Django 4.1
- uWSGI 2.0.21
## Development 
- `git clone git@github.com:barabashka25219/Learning-Log.git` (SSH)
- `git clone https://github.com/barabashka25219/Pizza.git`    (HTTPS)
- `conda env create -f environment.yml`
- `conda activate Pizza`
### Add package 
- `conda search $PACKAGE`
> Show available version of a packet 
- `conda install -n Pizza $PACKAGE[=$VERSION]`
- `conda list -n Pizza $PACKAGE`
> Make sure that the packet is installed in your environment via this command
- `conda env export > environment.yml`
- `git commit -m "Add $PACKET in environment"`
- `git push origin $BRANCH`
## Work with project
- `python Pizza/manage.py migrate`
- `python Pizza/manage.py createsuperuser`
