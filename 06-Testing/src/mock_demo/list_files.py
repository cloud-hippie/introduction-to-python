import subprocess

def list_files():
    """List files in the current directory"""
    return subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')
