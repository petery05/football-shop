document.addEventListener('DOMContentLoaded', () => {
    // Pilih semua elemen toast saat halaman dimuat
    const toastComponent = document.getElementById('toast-component');
    const toastIcon = document.getElementById('toast-icon');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastCloseButton = document.getElementById('toast-close-button');
    
    let hideTimeout;

    // Definisikan ikon untuk setiap tipe notifikasi
    const icons = {
        success: `<svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`,
        error: `<svg class="w-6 h-6 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`,
        info: `<svg class="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`,
    };

    // Fungsi untuk menyembunyikan toast
    function hideToast() {
        if (!toastComponent) return;
        toastComponent.classList.add('opacity-0', 'translate-x-full'); // Animasi ke kanan
        clearTimeout(hideTimeout);
    }

    // Fungsi utama untuk menampilkan toast
    function showToast(title, message, type = 'info', duration = 5000) {
        if (!toastComponent) return;

        clearTimeout(hideTimeout);

        // Atur konten dan ikon berdasarkan parameter
        toastTitle.textContent = title;
        toastMessage.textContent = message;
        toastIcon.innerHTML = icons[type] || icons.info;

        // Tampilkan toast dengan animasi dari kanan ke kiri
        toastComponent.classList.remove('opacity-0', 'translate-x-full');
        
        // Atur timer untuk menyembunyikan toast secara otomatis
        hideTimeout = setTimeout(() => {
            hideToast();
        }, duration);
    }

    // Tambahkan event listener untuk tombol tutup
    if (toastCloseButton) {
        toastCloseButton.addEventListener('click', hideToast);
    }

    // Jadikan fungsi showToast bisa diakses secara global
    window.showToast = showToast;
});