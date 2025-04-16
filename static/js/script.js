async function copyToClipboard(elementId, feedbackId) {
    try {
        const element = document.getElementById(elementId);
        const text = element.innerText;
        await navigator.clipboard.writeText(text);
        
        const feedback = document.getElementById(feedbackId);
        feedback.textContent = 'Disalin!';
        feedback.classList.add('show-feedback');

        setTimeout(() => {
            feedback.classList.remove('show-feedback');
        }, 2000);
    } catch (err) {
        console.error('Gagal menyalin teks: ', err);
    }
}

async function pasteToInput(inputId) {
    try {
        const text = await navigator.clipboard.readText();
        document.getElementById(inputId).value = text;
    } catch (err) {
        console.error('Gagal membaca clipboard: ', err);
    }
}
