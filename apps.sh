#!/usr/bin/env bash

echo 'Running App-1 🚀'
echo '****** <<<Package-1📦>>> ******'
echo 'Module-1 📚'
python src/app1/package1/module1.py
echo 'Module-2 📚'
python src/app1/package1/module2.py
echo '****** <<<Package-2📦>>> ******'
echo 'Module-1 📚'
python src/app1/package2/module1.py
echo 'Module-2 📚'
python src/app1/package2/module2.py

echo 
echo 'Running App-2 🚀'
echo '****** <<<Package-1📦>>> ******'
echo 'Module-1 📚'
python src/app2/package1/module1.py
echo 'Module-2 📚'
python src/app2/package1/module2.py
echo '****** <<<Package-2📦>>> ******'
echo 'Module-1 📚'
python src/app2/package2/module1.py
echo 'Module-2 📚'
python src/app2/package2/module2.py