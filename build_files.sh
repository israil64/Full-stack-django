
echo "BUILD START"
source "C:\Users\DELL\OneDrive\Desktop\Django Fullstack\.venv\Scripts\activate"
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"