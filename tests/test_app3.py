import sys

app = 'App=3'

try:
    sys.path.insert(1, '../')
    import src.app3.package1 as pckg_1
except ModuleNotFoundError:
    sys.path.insert(1, '')
    import src.app3.package1 as pckg_1
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')

print(pckg_1)
