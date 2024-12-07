# Todo List

## App Todo
- ### Lengkapi fungsi utama
    - Simpan models di directory `assets`
    - Pastikan fungsi utama memiliki input type `PIL.Image.Image` dari `pillow`
    - Pastikan return value berupa instance dari class `Result` pada module `plant_scanner.models`.
    - Lakukan testing dan pastikan library berjalan dengan baik

## Build Todo
- Pastikan semua dependency ada di `requirements.txt` atau `Pipfile`
- Pastikan versi `tensorflow` terdefinisi lengkap di `requirements.txt` atau `Pipfile`
- Gunakan git tag untuk versi library
- Konfigurasi `setup.py`
- Pastikan library bisa di build dengan:
```bash
python setup.py sdist bdist_wheel
```
- Pastikan library bisa diinstal dengan:
```bash
pip install git+https://github.com/AgroTention-Project/plant-scanner-app.git
```

