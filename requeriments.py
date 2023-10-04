import sys
import importlib
import subprocess
import pkg_resources
from config.libraries_descryption import list_libraries
from config.display_descryption import SEPARATOR, SLEEP_TIME
from config.crawler_descryption import SCHEDULE
import time

def checkLibraries():
    print(SEPARATOR)
    for library_name, library_import in list_libraries.items():
        try:
            importlib.import_module(library_name)
            installed_version = pkg_resources.get_distribution(library_import).version
            print(f'{library_name} is installed (Version: {installed_version})')
            
            # Check for the latest version on PyPI
            latest_version = subprocess.check_output([sys.executable, "-m", "pip", "show", library_import]).decode("utf-8")
            latest_version = [line for line in latest_version.split('\n') if line.startswith('Version:')]
            if latest_version:
                latest_version = latest_version[0].split(':', 1)[1].strip()
                if installed_version != latest_version:
                    print(f'A newer version ({latest_version}) is available. Updating...')
                    try:
                        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", library_import])
                        print(f'{library_name} has been updated to version {latest_version}.')
                    except Exception as e:
                        print(f'Error updating {library_name}: {e}')
            else:
                print(f'Could not fetch latest version information for {library_name}')
        except ImportError as e:
            print(f'{library_name} is not installed')
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", library_import])
                print(f'{library_name} has been installed.')
            except Exception as e:
                print(f'Error installing {library_name}: {e}')
                exit(1)
        except pkg_resources.DistributionNotFound:
            print(f'Missing dependencies for {library_name}. Updating...')
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", library_import])
                print(f'{library_name} and its dependencies have been updated.')
            except Exception as e:
                print(f'Error updating {library_name} and its dependencies: {e}')
    print(SEPARATOR)
    if SCHEDULE == True:
        time.sleep(SLEEP_TIME)
    else:
        input("Press enter to continue...")