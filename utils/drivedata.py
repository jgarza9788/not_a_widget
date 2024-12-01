import shutil

def get_drivedata(path):
    """Get the total, used, and free space of the drive that contains the given path, formatted in gigabytes."""
    total, used, free = shutil.disk_usage(path)
    total_gb = total / (1024**3)
    used_gb = used / (1024**3)
    free_gb = free / (1024**3)

    result = {}
    result['used_gb'] = used_gb
    result['free_gb'] = free_gb
    result['total_gb'] = total_gb
    result['percent'] = used_gb/total_gb


    return result



if __name__ == '__main__':

    print(get_drivedata('/media/jgarza/SSD'))