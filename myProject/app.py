import streamlit as st
import base64

def caesar_encrypt(text, shift):
    """
    Fungsi untuk mengenkripsi teks menggunakan Caesar Cipher
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_base + shift) % 26 + ascii_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    """
    Fungsi untuk mendekripsi teks Caesar Cipher
    """
    return caesar_encrypt(encrypted_text, -shift)

def base64_encrypt(text):
    """
    Fungsi untuk mengenkripsi teks menggunakan Base64
    """
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')

def base64_decrypt(encrypted_text):
    """
    Fungsi untuk mendekripsi teks Base64
    """
    try:
        base64_bytes = encrypted_text.encode('utf-8')
        text_bytes = base64.b64decode(base64_bytes)
        return text_bytes.decode('utf-8')
    except:
        return "Error: Invalid Base64 string"

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Enkripsi & Dekripsi Text",
    page_icon="🔐",
    layout="wide"
)

# Judul aplikasi
st.title("🔐 Aplikasi Enkripsi dan Dekripsi Text")
st.write("Aplikasi ini dapat mengenkripsi dan mendekripsi teks menggunakan metode Caesar Cipher atau Base64.")

# Membuat tab untuk enkripsi dan dekripsi
tab1, tab2 = st.tabs(["Enkripsi", "Dekripsi"])

# Tab Enkripsi
with tab1:
    st.header("Enkripsi Text")
    
    # Input teks untuk dienkripsi
    text_to_encrypt = st.text_area("Masukkan teks yang akan dienkripsi:", height=100)
    
    # Pilihan metode enkripsi
    encryption_method = st.radio(
        "Pilih metode enkripsi:",
        ["Caesar Cipher", "Base64"]
    )
    
    # Parameter tambahan untuk Caesar Cipher
    if encryption_method == "Caesar Cipher":
        shift = st.slider("Pilih jumlah pergeseran:", 1, 25, 3)
    
    # Tombol enkripsi
    if st.button("Enkripsi", key="encrypt_button"):
        if text_to_encrypt:
            if encryption_method == "Caesar Cipher":
                result = caesar_encrypt(text_to_encrypt, shift)
                st.success("Teks berhasil dienkripsi!")
                st.code(result)
                st.info(f"Kunci pergeseran: {shift} (simpan untuk dekripsi)")
            else:  # Base64
                result = base64_encrypt(text_to_encrypt)
                st.success("Teks berhasil dienkripsi!")
                st.code(result)
        else:
            st.warning("Mohon masukkan teks terlebih dahulu!")

# Tab Dekripsi
with tab2:
    st.header("Dekripsi Text")
    
    # Input teks untuk didekripsi
    text_to_decrypt = st.text_area("Masukkan teks yang akan didekripsi:", height=100)
    
    # Pilihan metode dekripsi
    decryption_method = st.radio(
        "Pilih metode dekripsi:",
        ["Caesar Cipher", "Base64"],
        key="decrypt_radio"
    )
    
    # Parameter tambahan untuk Caesar Cipher
    if decryption_method == "Caesar Cipher":
        decrypt_shift = st.slider("Masukkan kunci pergeseran:", 1, 25, 3, key="decrypt_slider")
    
    # Tombol dekripsi
    if st.button("Dekripsi", key="decrypt_button"):
        if text_to_decrypt:
            if decryption_method == "Caesar Cipher":
                result = caesar_decrypt(text_to_decrypt, decrypt_shift)
                st.success("Teks berhasil didekripsi!")
                st.code(result)
            else:  # Base64
                result = base64_decrypt(text_to_decrypt)
                if result.startswith("Error"):
                    st.error(result)
                else:
                    st.success("Teks berhasil didekripsi!")
                    st.code(result)
        else:
            st.warning("Mohon masukkan teks terlebih dahulu!")

# Informasi tambahan
with st.expander("ℹ️ Informasi Tambahan"):
    st.markdown("""
    ### Tentang Metode Enkripsi:
    
    1. **Caesar Cipher**
       - Metode enkripsi sederhana yang menggeser setiap huruf dalam alfabet sejumlah posisi tertentu
       - Mempertahankan huruf besar/kecil dan karakter non-alfabet
       - Memerlukan kunci pergeseran (1-25) untuk enkripsi dan dekripsi
    
    2. **Base64**
       - Metode encoding yang mengubah data biner menjadi teks ASCII
       - Tidak memerlukan kunci
       - Sering digunakan untuk mengirim data biner melalui media yang hanya mendukung teks
    
    ### Cara Penggunaan:
    1. Pilih tab Enkripsi atau Dekripsi
    2. Masukkan teks yang ingin diproses
    3. Pilih metode enkripsi/dekripsi
    4. Untuk Caesar Cipher, atur jumlah pergeseran
    5. Klik tombol Enkripsi/Dekripsi
    """)

# Footer
st.markdown("---")
st.markdown("            Copyright by Ruleks")