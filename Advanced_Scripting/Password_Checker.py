import requests
import hashlib
import sys

def request_apidata(hash_char):
    url = 'https://api.pwnedpasswords.com/range/'+ hash_char
    res = requests.get(url)
    if res.status_code!= 200:
        raise RuntimeError(f'Error fetching:{res.status_code}, check the API and try again')
    return res

def get_pwned_count(hashlist, hashtail):
    hashline = (line.split(':') for line in hashlist.splitlines()) # splits the entire string in individul lines and then splits them into list of strings 
    for h,count in hashline:
        if h == hashtail:
            return count
    return 0

def pwned_apicheck(password):
    sha1pwd = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper() # code to fetch hashed string equivalent to the input password
    F5_hashhead, F5_hashtail = sha1pwd[:5],sha1pwd[5:] # string operation to split the hash string into head (5) and tail (rest)
    res = request_apidata(F5_hashhead) # API call to pull all the hash strings that matches the first 5 hash input
    return get_pwned_count(res.text,F5_hashtail) # generator object to call the method that returns the total count of match with hash string

def main(args):
    for password in args:
        count = pwned_apicheck(password)
        if count: print(f'{password} was found {count} times')
        else: print(f'{password} not found. Good to go!')
    return 'Completed'

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))
