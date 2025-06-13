import pikepdf
from tqdm import tqdm  # Optional: for progress bar

def brute_force_pdf_password(pdf_path):
    for i in tqdm(range(10000), desc="Trying passwords"):
        password = f"{i:04d}"  # formats numbers like 0000, 0001, ..., 9999
        try:
            with pikepdf.open(pdf_path, password=password) as pdf:
                print(f"\n✅ Password found: {password}")
                pdf.save("unlocked_output.pdf")
                return
        except pikepdf.PasswordError:
            continue
    print("❌ Password not found in range 0000-9999.")

# Set the actual file path
pdf_path = "/Users/macbook/PythonProjects/pdf_bank.pdf"
brute_force_pdf_password(pdf_path)
