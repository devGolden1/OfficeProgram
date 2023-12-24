import tkinter as tk
from tkinter import filedialog

class MetinDuzenleyici:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Metin Düzenleyici")

        self.metin_alani = tk.Text(self.pencere, wrap="word")
        self.metin_alani.pack(expand=True, fill="both")

        menu_bar = tk.Menu(self.pencere)
        self.pencere.config(menu=menu_bar)

        dosya_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Dosya", menu=dosya_menu)
        dosya_menu.add_command(label="Aç", command=self.dosya_ac)
        dosya_menu.add_command(label="Kaydet", command=self.dosya_kaydet)
        dosya_menu.add_separator()
        dosya_menu.add_command(label="Çıkış", command=self.pencere.destroy)

    def dosya_ac(self):
        dosya_adi = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
        if dosya_adi:
            with open(dosya_adi, "r") as dosya:
                icerik = dosya.read()
                self.metin_alani.delete(1.0, tk.END)
                self.metin_alani.insert(tk.END, icerik)

    def dosya_kaydet(self):
        dosya_adi = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
        if dosya_adi:
            with open(dosya_adi, "w") as dosya:
                dosya.write(self.metin_alani.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = MetinDuzenleyici(root)
    root.mainloop()
