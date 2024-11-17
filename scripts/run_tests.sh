coverage run -m pytest
if [ $? -eq 0 ]; then
    coverage html && open htmlcov/index.html
else
    echo "Tests failed. Coverage report not generated."
fi