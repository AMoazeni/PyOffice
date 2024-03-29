from time import time as t
from urllib.request import urlopen as get

def OpenFile(*args, **kwargs):
    
    ''' OpenFile(str 'file_path') requires an 'str' PATH or URL input,
        returns a Python Dictionary with the file data. 
    '''
    
    # Initialize
    func_name = 'OpenFile'
    print(func_name, '[START]')
    if args: print(func_name, 'Path:', args[0])
    time_start = t()
    error = 0
    error_msg = ''
    
    path = ''
    data = {}
    data_len = 0
    
    # OpenFile Function Block
    try:
        path = str(args[0])
        data['Data'] = []
        
        # PATH is a URL.
        if 'http' in path.lower():
            page = get(path)
            page_code = page.getcode()
            data['ResponseCode'] = page_code
            page_headers = page.getheaders()
            data['Headers'] = page_headers
            for line in page.readlines():
                data['Data'].append(line.decode('utf-8'))
                data_len = data_len + len(str(line))
                
        # PATH is a local file.        
        else:
            with open(path, 'r', encoding="utf-8") as file:
                for line in file:
                    data['Data'].append(line)
                    data_len = data_len + len(line)
        
        
        data['TimeStart'] = float(round(time_start, 4))
        data['TimeEx'] = float(round(t() - time_start, 4))
        data['Path'] = path
        data['Name'] = path.split('/')[-1]
        data['Extension'] = path.split('.')[-1]
        data['Lines'] = len(data['Data'])
        data['DataLength'] = data_len
        
        return data

    # Error Handler
    except BaseException as e:
        error = 1
        error_msg = str(e)

    
    # Clean up block
    finally:
        if error:
            print(func_name, '[ERROR]:', error_msg)
        else:
            print(func_name, '[OK] {0:.3f}s\n'.format(float(t() - time_start)))
        pass



