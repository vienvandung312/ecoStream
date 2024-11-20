coverage run -m pytest
if [ $? -eq 0 ]; then
    coverage html && coverage report && open htmlcov/index.html
else
    echo "Tests failed. Coverage report not generated."
fi